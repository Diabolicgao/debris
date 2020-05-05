from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('personal_information/', views.Info, name = 'info'),
    path('order/', views.OrderUser, name = 'order'),
    path('order/delete_order/<int:pk>/', views.DeleteOrder, name = 'delete_order'),
    path('change_pass/', auth_views.PasswordChangeView.as_view(template_name = 'pages/change_pass.html',success_url = '/', extra_context = {'title':'Thành công'}), name = 'change_pass'),
    path('address/', views.Address, name = 'address'),
    path('address/add_address/', views.AddAddress, name = 'add_address'),
    path('address/update_address/<int:pk>/', views.UpdateAddress, name = 'update_address'),
    path('address/delete_address/<int:pk>/', views.DeleteAddress, name = 'delete_address'),
]