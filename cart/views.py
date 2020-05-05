from django.shortcuts import render,get_object_or_404
from data.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import OrderForm
# Create your views here.
 
def CartObj(request) :
    # Get User Object
    User_Obj = request.user
    # Get Model Cart in User
    Cart_Obj = User_Obj.cart.all()    
    # Get Model InfoUser in User
    if User_Obj.info.all() :
        InfoUser_Obj = User_Obj.info.get(default = True)
    else :
        InfoUser_Obj = None
    # Get amount model Cart
    count_cart = User_Obj.cart.all().count()

    n = 0
    Sum = 0
    Charge = 0
    for i in User_Obj.cart.all() :
        n += i.price 
    
    if n > 1000000 :
        Sum = n 
    else :
        Charge += 19000
        Sum = n + Charge

    formOrder = OrderForm()
    if request.method == 'POST' :
        formOrder = OrderForm(request.POST, user = request.user, address = InfoUser_Obj.address, phonenumber = InfoUser_Obj.phonenumber,sum_money = n, tran_cost = Charge)
        if formOrder.is_valid() :
            Order_Obj = formOrder.save()
            for i in Cart_Obj :
                cart_order = CartOrder(order = Order(pk = Order_Obj.pk), item = i.item, price = i.price, amount = i.amount)
                cart_order.save()
            User_Obj.cart.all().delete()
            return HttpResponseRedirect("/user/order/")

    Data = {
        'count_cart' : count_cart,
        'all' : User_Obj.cart.all(),
        'myUser' : User_Obj, 
        'n' : n,
        'Sum' : Sum,
        'Charge' : Charge,
        'formOrder' : formOrder,
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }

    try:
        myUser = User.objects.get(username = request.user)
        info = myUser.info.filter(default = True)
        Data['info'] = info
    except User.DoesNotExist:
        info = None

    return render(request, "pages/cart.html", Data)

def Delete(request, pk) :
    myUser = User.objects.get(username = request.user)
    myUser.cart.get(pk = pk).delete()
    return HttpResponseRedirect('/cart/')

    count_cart = myUser.cart.all().count()
    
    Data = {
        'count_cart' : count_cart,
        'all' : myUser.cart.all()
    }
    return render(request, "pages/cart.html", Data)

def Item(request, item) :
    myUser = User.objects.get(username = request.user)
    cart_obj = myUser.cart.filter(item = item)
    item = ''
    for i in cart_obj :
        item += i.item
        break 
    post_obj = Post.objects.get(title = item)
    url = '/category/{}'.format(post_obj.id)
    return HttpResponseRedirect(url)
    # return render(request, "pages/post.html")


