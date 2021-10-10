from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import Item


def basket_contents(request):
    '''
    Create the basket contents, used
    throughout the site
    '''
    basket_items = []
    total = 0
    item_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        item = get_object_or_404(Item, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item': item
        })

    if total < settings.FREE_DELIVERY_OUTSET:
        delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_eligibility = settings.FREE_DELIVERY_OUTSET - total
    else:
        delivery_cost = 0
        free_delivery_eligibility = 0

    sum_total = delivery_cost + total
   
    context = {
        'basket_items': basket_items,
        'total': total,
        'item_count': item_count,
        'delivery_cost': delivery_cost,
        'free_delivery_eligibility': free_delivery_eligibility,
        'free_delivery_outset': settings.FREE_DELIVERY_OUTSET,
        'sum_total': sum_total,
    }

    return context

