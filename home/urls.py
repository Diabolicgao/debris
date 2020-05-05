from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from access import views as views_ac
urlpatterns = [
    path('', views.Home),
    path('about/', views.About, name = 'about'),
    path('author/', views.Author, name = 'author'),
    path('blank/', views.Blank, name = 'blank'),
    path('blog/', views.Blog, name = 'blog'),
    path('contact/', views.Contact, name = 'contact'),
]