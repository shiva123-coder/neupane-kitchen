from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q
from .models import Item, Category
from profiles.models import UserProfile

from reviews.forms import ReviewForm
from reviews.models import Review


def all_menu(request):
    """
    A view to return the items.
    view also include sorting and seaching
    """
    items = Item.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    # code taken from walktrough project of CI and modified (start)
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == "name":
                items = items.annotate(sortkey=Lower("name"))

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == 'desc':
                    sortkey = f"-{sortkey}"

            if sortkey == "None":
                items = items
            else:
                items = items.order_by(sortkey)
            
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            items = items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if request.GET:
            if 'q1' in request.GET:
                query = request.GET['q1']
                if not query:
                    messages.error(request, "No search criteria entered!")
                    return redirect(reverse('all_menu'))
                
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                items = items.filter(queries)

    existing_sorting = f'{sort}_{direction}'
    # code taken from walktrough project of CI and modified (End)
    context = {
        'items': items,
        'search_term': query,
        'existing_categories': categories,
        'existing_sorting': existing_sorting,
    }
    return render(request, 'menu/menu.html', context)


def item_info(request, item_id):
    """ A view to render individual item details from menu """

    item = get_object_or_404(Item, pk=item_id)
    review = Review.objects.filter(item=item)
    review_form = ReviewForm()

    context = {
        'item': item,
        "review": review,
        "review_form": review_form,
    }

    return render(request, 'menu/item_info.html', context)