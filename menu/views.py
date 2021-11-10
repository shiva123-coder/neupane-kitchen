from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q
from .models import Item, Category
from profiles.models import UserProfile

from reviews.forms import ReviewForm
from reviews.models import Review
from .forms import ItemForm


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
    reviews = Review.objects.filter(item=item)
    review_form = ReviewForm()

    context = {
        'item': item,
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'menu/item_info.html', context)


def add_item(request):
    """
    add item to the page
    option only for superuser
    """
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Thank you!, Item added succesfully!')
            return redirect(reverse('all_menu'))
        else:
            messages.error(request,
                           ('Sorry! Something went wrong,\
                                Please recheck the form and try again.'))
    else:
        form = ItemForm()

    template = 'menu/add_item.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_item(request, item_id):
    """edit/update item and its info from the page"""
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item updated!')
            return redirect(reverse('item_info', args=[item.id]))
        else:
            messages.error(request, 'Sorry, request failed, please re-check the form and try again')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'menu/edit_item.html'
    context = {
        'form': form,
        'item': item,
        'on_edit_page': True
    }

    return render(request, template, context)


def delete_item(request, item_id):
    """ Delete item from the page """
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('all_menu'))