from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('post_info/<int:post_id>/', views.post_info, name='post_info'),
]
