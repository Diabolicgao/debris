from django.shortcuts import render
from django.shortcuts import render
from data.models import *
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def Error(request, exception) :
    exception = "Lỗi 404 "
    Data = {
        "message" : exception,
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }
    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None
    return render(request, "displayerror/error.html", Data)