from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from menu.models import Item
from basket.contexts import basket_contents


import stripe
import json


@require_POST
def cache_checkout_data(request):
    """ view to cache data once checkout form submitted"""
    try:
        payment_intent_id = request.POST.get(
            "client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(payment_intent_id, metadata={
            "username": request.user,
            "save_info": request.POST.get("save_info"),
            "basket": json.dumps(request.session.get("basket", {}))
        })

        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, "Sorry! your payment \
            can't be proceeed right now. Please try again later.")
        return HttpResponse(content=e, status=400)
   

def checkout_card(request):
    """ card checkout page view """
    # stripe  variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "contact_number": request.POST["contact_number"],
            "street_address": request.POST["street_address"],
            "postal_code": request.POST["postal_code"],
        }

        order_form = OrderForm(form_data)

        # order create once valid form sent
        if order_form.is_valid():
            order = order_form.save()

            for item_id, quantity in basket.items():
                try:
                    item = Item.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        quantity=quantity,
                        )
                    order_line_item.save()

                # item not found
                except Item.DoesNotExist:
                    messages.error(request, (
                        "Sorry ! Item not found.\
                           You may need to contat support team"
                    ))
                    order.delete()
                    return redirect(reverse('view_basket'))

            # save the users info
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, "Theres was an error.\
                Please re-check the information")

    current_basket = basket_contents(request)
    total = current_basket['sum_total']
    stripe_total = round(total * 100)

    # stripe payment intent
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)

            # name_of_user = profile.user_full_name
            # address_of_user = profile.user_address

            order_form = OrderForm(initial={
                'full_name': profile.user_full_name,
                'email': profile.user.email,
                'contact_number': profile.user_contact_number,
                'street_address': profile.user_address,
                'postal_code': profile.user_postal_code,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    # warning message, if forgot to set stripe public key
    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing,\
             please set public key to your environment")

    template = 'checkout/checkout_card.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_cash(request):
    """ cash checkout page view """
    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "contact_number": request.POST["contact_number"],
            "street_address": request.POST["street_address"],
            "postal_code": request.POST["postal_code"],
        }

        order_form = OrderForm(form_data)
        # order create once valid form sent
        if order_form.is_valid():
            order = order_form.save()

            for item_id, quantity in basket.items():
                try:
                    item = Item.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        quantity=quantity,
                        )
                    order_line_item.save()

                # item not found
                except Item.DoesNotExist:
                    messages.error(request, (
                        "Sorry ! Item not found.\
                           You may need to contat support team"
                    ))
                    order.delete()
                    return redirect(reverse('view_basket'))

            # save the users info
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, "Theres was an error.\
                Please re-check the information")

    current_basket = basket_contents(request)
    total = current_basket['sum_total']

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user_full_name,
                'email': profile.user.email,
                'contact_number': profile.user_contact_number,
                'street_address': profile.user_address,
                'postal_code': profile.user_postal_code,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    template = 'checkout/checkout_cash.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    view when checkout successful
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # connect user's profile to the order
        order.user_profile = profile
        order.save()

        # save user's info
        if save_info:
            profile_data = {
                'user_full_name': order.full_name,
                'user_contact_number': order.contact_number,
                'user_address': order.street_address,
                'user_postal_code': order.postal_code,
            }

            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Thank you ! order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
      'order': order,
    }

    return render(request, template, context)

