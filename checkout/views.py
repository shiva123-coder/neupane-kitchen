from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm



def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's no items in your bag at the moment")
        return redirect(reverse('all_menu'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JiFwUIpMq2ondKYU9lCh9Y8Fo9WFnii1hIpX2y1N2WzcJAGnTIOg9kGD2MODjOk1PI0apL6VlVlT2hkBaukCOh700Twlnv49Z',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
