from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('post_info/<int:post_id>/', views.post_info, name='post_info'),
    path('delete_comment/<post_id>', views.delete_comment, name='delete_comment'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
