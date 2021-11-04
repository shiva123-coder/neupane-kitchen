from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import ReviewForm
from .models import Review


def food_reviews(request):
    """show all reviews"""
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewing_user = request.user
            review.rating = int(request.POST.get('rating'))
            review.save()
            
    reviews = Review.objects.all()
    p = Paginator(reviews, 8)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    form = ReviewForm()
    template = "reviews/food_reviews.html"

    context = {
        'form': form,
        'page_obj': page_obj,
    }

    return render(request,
                  template,
                  context)
