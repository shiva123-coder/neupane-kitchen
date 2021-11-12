from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    # path("post/<int:post_id>/", views.view_post, name="view_post"),
]