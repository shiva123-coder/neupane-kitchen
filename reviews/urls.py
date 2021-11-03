from django.urls import path
from . import views

urlpatterns = [
    path("", views.food_reviews, name="food_reviews"),
]