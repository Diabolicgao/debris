from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.Event_Notify, {'Obj' : 'event'}, name = 'event'),
    path('notify/', views.Event_Notify, {'Obj' : 'notify'}, name = 'notify'),
    path('<int:pk>/', views.Post_Event, name = 'post_event'),
]