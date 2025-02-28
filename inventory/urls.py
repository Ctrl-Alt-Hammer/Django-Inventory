from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.inventory_list, name='list'),
    path('add_new_item/', views.new_item, name='new_item'),
    path('<slug:slug>', views.inventory_page, name='page'),
]
