from django.shortcuts import render, get_object_or_404
from data.models import *
# Create your views here.

def Event_Notify(request, Obj) :
    Data = {
        'Obj' : Event.objects.filter(category = Obj).order_by('-time'),
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }
    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None
    return render(request, 'pages/event.html', Data)

def Post_Event(request, pk) :
    Obj = get_object_or_404(Event, pk = pk)
    Data = {
        'Obj' : Obj,
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }
    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None
    return render(request, 'pages/post_event.html', Data)