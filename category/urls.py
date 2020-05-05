from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.Category, {'Obj' : ''}, name = 'all'),
    path('city/', views.Category, {'Obj' : 'city'}, name = 'city'),
    path('cyberpunk/', views.Category, {'Obj' : 'cyberpunk'}, name = 'cyberpunk'),
    path('custom/', views.Category, {'Obj' : 'custom'}, name = 'custom'),
    path('star_wars/', views.Category, {'Obj' : 'star_wars'}, name = 'star_wars'),
    path('ninjago/', views.Category, {'Obj' : 'ninjago'}, name = 'ninjago'),
    path('dc/', views.Category, {'Obj' : 'dc'}, name = 'dc'),
    path('marvel/', views.Category, {'Obj' : 'marvel'}, name = 'marvel'),
    path('overwatch/', views.Category, {'Obj' : 'overwatch'}, name = 'overwatch'),
    path('vehicle/', views.Category, {'Obj' : 'vehicle'}, name = 'vehicle'),
    path('technic/', views.Category, {'Obj' : 'technic'}, name = 'technic'),
    path('animal/', views.Category, {'Obj' : 'animal'}, name = 'animal'),
    path('dragon/', views.Category, {'Obj' : 'dragon'}, name = 'dragon'),
    path('castle/', views.Category, {'Obj' : 'castle'}, name = 'castle'),
    path('fantasy/', views.Category, {'Obj' : 'fantasy'}, name = 'fantasy'),
    path('item/', views.Category, {'Obj' : 'item'}, name = 'item'),
    path('brick/', views.Category, {'Obj' : 'brick'}, name = 'brick'),

    path('<int:pk>/', views.PostObj, name = 'post'),
]