from decimal import Decimal
from django.conf import settings


def basket_contents(request):
    '''
    Create the basket contents, used
    throughout the site
    '''
    basket_items = []
    total = 0
    item_count = 0

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

