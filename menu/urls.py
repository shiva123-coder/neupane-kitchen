from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_menu, name='menu'),
    path('<item_id>', views.item_info, name='item_info'),
]

