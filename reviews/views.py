from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import ReviewForm
from .models import Review
from django.db.models import Avg

from menu.models import Item
from profiles.models import UserProfile


def add_review(request, item_id):
    """view to add reviews"""
    item = get_object_or_404(Item, pk=item_id)
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            comment = form.cleaned_data['comment']
            rating = form.cleaned_data['rating']
            Review.objects.create(
                reviewer=user,
                item=get_object_or_404(Item, pk=item_id),
                title=title,
                rating=rating,
                comment=comment)
            messages.success(request, 'Revied added.')
            return redirect(reverse('item_info', args=[item_id]))
        else:
            messages.error(request, 'Sorry! we are unable to add your review. \
                    Please check your input and try again')
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


