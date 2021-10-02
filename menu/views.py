from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category

def all_menu(request):
    """ A view to return the items """

    items = Item.objects.all()
    
    context = {
        'items': items,
    }
    return render(request, 'menu/menu.html', context)



def item_info(request, item_id):
    """ A view to render individual item details from menu """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'menu/item_info.html', context)
