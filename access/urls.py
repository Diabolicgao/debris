from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from access import views as views_ac

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = "pages/sign_in.html"), name = "sign_in"),
    path('logout/', auth_views.LogoutView.as_view(next_page = "/"), name = 'sign_out'),
    path('logup/', views_ac.Register, name = 'sign_up'),
]