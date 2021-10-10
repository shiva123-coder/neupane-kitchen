from django.shortcuts import render, redirect, get_object_or_404, reverse
from menu.models import Item
from django.contrib import messages


def view_basket(request):
    """ render the shopping basket page """
    
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """add quantity of selected item to the basket"""
    quantity = int(request.POST.get('quantity'))    
    # redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def update_basket(request, item_id):
    """update the quantity of the selected product in the basket"""
    if request.method == "POST":
        item = get_object_or_404(Item, pk=item_id)
        quantity = int(request.POST.get("quantity"))

        basket = request.session.get("basket", {})

        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request,
                             f"{item.name}'s \
 quantity has been updated to {basket[item_id]}")
        else:
            basket.pop(item_id)
            messages.success(request,
                             f"{item.name} has been removed from your cart.")

        request.session["cart"] = basket

        return redirect(reverse("view_basket"))
    else:
        messages.error(request, "Error!  you do not have permission perform this action.")
        return redirect(reverse("home_page"))

         
