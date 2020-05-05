from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartObj, name = 'cart'),
    path('<int:pk>/', views.Delete, name = 'delete'),
    path('<str:item>/', views.Item),
]