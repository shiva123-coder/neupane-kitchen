from django.shortcuts import render
from .forms import ReviewForm
from .models import Review


def food_reviews(request):
    """show all reviews"""

    form = ReviewForm(request.POST)
    reviews = Review.objects.all()

    template = "reviews/food_reviews.html"

    context = {
        "form": form,
    }

    return render(request,
                  template,
                  context)
