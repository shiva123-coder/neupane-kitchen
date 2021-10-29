from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages

from checkout.models import Order


def profile(request):
    """
    Display user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/user_profile.html'

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Thank you ! Your profile has been updated successfully")
        else:
            messages.error(request,
                           "Sorry! your details can't be save now,\
                            please re-check the input and try again")

    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    context = {
        'form': form,
        'orders': orders,
        "on_profile_page": True,
    }
        
    return render(request, template, context)


def order_history(request, order_number):
    """
    display the users previous order
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, "This is your order from past")

    template = "profiles/order_history.html"
    
    context = {
        "order": order,
        "past_order": True,
    }

    return render(request,
                  template,
                  context)