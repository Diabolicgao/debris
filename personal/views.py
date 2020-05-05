from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from data.models import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from .forms import UpdateInfoUserForm, InfoForm
# Create your views here.

# ------>>> Info <<<------\
def Info(request) :
    Data = {
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }

    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None

    return render(request, 'pages/info.html', Data)
# --------------------------/

# ------>>> Address <<<------\
def Address(request) :
    user = request.user
    all_address = user.info.all()
    
    if all_address.count() == 1 :
        for i in all_address :
            i.default = True
            i.save()
            
    Data = {
        'all_address' : all_address,
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }

    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None

    return render(request, 'pages/address.html', Data)
# -----------------------------/

# ------>>> Oreder <<<------\
def OrderUser(request) : 
    Data = {
        "all_order" : Order.objects.filter(user = request.user).exclude(Q(cancel = True) | Q(exchange_scf = True)).order_by('-time'),
        "exchange_scf" : Order.objects.filter(user = request.user, exchange_scf = True).order_by('-time'),
        "cancel" : Order.objects.filter(user = request.user, cancel = True).order_by('-time'),
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }

    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None

    return render(request, 'pages/order.html', Data)
# ----------------------------/

# ------>>> Add Address <<<------\
def AddAddress(request) :
    form = InfoForm()
    if request.method == 'POST' :
        form = InfoForm(request.POST, user = request.user, default = False)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect("/user/address/")

    Data = {
        'form' : form,
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }

    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None

    return render(request, 'pages/add_address.html', Data)
# ----------------------------------/

# ------>>> Update Address <<<------\
def UpdateAddress(request, pk) :
    info_obj = get_object_or_404(InfoUser, pk= pk)
    form = UpdateInfoUserForm()
    
    if request.method == 'POST' :
        form = UpdateInfoUserForm(request.POST)
        if form.is_valid() :
            info_obj.address = form.cleaned_data['address']
            info_obj.phonenumber = form.cleaned_data['phonenumber']
            info_obj.default = form.cleaned_data['default']
            if info_obj.default :
                user = request.user
                user_info = user.info.exclude(pk = pk)
                for i in user_info :
                    i.default = False
                    i.save()
            info_obj.save()

            return HttpResponseRedirect("/user/address/")

    Data = {
        'form' : form,
        'info_obj' : info_obj,
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }

    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None
        
    return render(request, 'pages/update_address.html', Data)
# ------------------------------------/

# ------>>> Delete Address <<<------\
def DeleteAddress(request, pk) :
    info_obj = get_object_or_404(InfoUser, pk= pk)
    info_obj.delete()

    return HttpResponseRedirect("/user/address/")
# ----------------------------------/

def DeleteOrder(request, pk) :
    Order_Obj = get_object_or_404(Order, pk = pk)
    Order_Obj.cancel = True
    Order_Obj.save()
    return HttpResponseRedirect("/user/order")

