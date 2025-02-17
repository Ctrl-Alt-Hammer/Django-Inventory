from django.urls import path

from . import views # import views from current directory

urlpatterns = [
    path('<int:item_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]