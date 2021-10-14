from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse)

from menu.models import Item
from django.contrib import messages


def view_basket(request):
    """ render the shopping basket page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """add quantity of selected item to the basket"""
    item = Item.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))    
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        messages.success(request, f'{item.name} added to your basket')

    request.session['basket'] = basket
    return redirect(reverse('all_menu'))


def update_basket(request, item_id):
    """update the quantity of the selected item in the basket"""
    if request.method == "POST":
        item = get_object_or_404(Item, pk=item_id)
        quantity = int(request.POST.get('quantity'))

        basket = request.session.get('basket', {})

        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request,
                             f"{item.name}'s \
 quantity has been updated to {basket[item_id]}")
        else:
            basket.pop(item_id)
            messages.success(request,
                             f"{item.name} has been removed from your basket.")

        request.session["basket"] = basket

        return redirect(reverse('view_basket'))
    else:
        messages.error(request, "Error!  you do not have permission perform this action.")
        return redirect(reverse('home'))


def remove_basket(request, item_id):
    """Remove item from the basket"""
    if request.method == "POST":
        try:
            item = get_object_or_404(Item, pk=item_id)

            basket = request.session.get('basket', {})

            basket.pop(item_id)
            messages.success(request,
                             f"{item.name} has now removed from your basket.")

            request.session["basket"] = basket
            return HttpResponse(status=200)

        except Exception as error:
            messages.error(request, f"Sorry, We have encountered an error while removing item {error}")
            return HttpResponse(status=500)

    else:
        messages.error(request, "Sorry! you are not authorised to perform this.")
        return redirect('home')