from django.shortcuts import render


def view_basket(request):
    """ A view to return the shopping basket """

    return render(request, 'basket/basket.html')
