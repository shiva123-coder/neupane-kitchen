def all_menu(request):
    """ A view to return the items """

    items = Item.objects.all()
    
    context = {
        'items': items,
    }
    return render(request, 'menu/menu.html', context)
