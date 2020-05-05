from django.shortcuts import render,get_object_or_404
from data.models import Event,Post
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from data.models import *
from django.http import HttpResponseRedirect
from .forms import CartForm, CommentForm
from django.contrib.auth.models import User
# Create your views here.

def Category(request, Obj) :
    if Obj == '' :
        Data_List = Post.objects.all().order_by('-time')
        query = request.GET.get('search')
        if query :
            Data_List = Post.objects.filter(title__icontains = query)    
    else :
        Data_List = Post.objects.filter(category = Obj).order_by('-time')
        query = request.GET.get('search')
        if query :
            Data_List = Post.objects.filter(title__icontains = query)

    page = request.GET.get('page', 1)

    paginator = Paginator(Data_List, 12)
    try :
        Data = paginator.page(page)
    except PageNotAnInteger :
        Data = paginator.page(1)
    except EmptyPage :
        Data = paginator.page(paginator.num_pages)

    Box = {
        "Data" : Data,
        'All' : Post.objects.all().count(),
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }
    AllCategory = [
        'city', 'cyberpunk', 'custom', 
        'star_wars', 'ninjago', 'dc', 
        'marvel', 'overwatch',
        'vehicle', 'technic', 'animal', 
        'dragon', 'castle', 'fantasy',
        'item', 'brick'
    ]
    for i in AllCategory :
        Box[i] = Post.objects.filter(category = i).count()

    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Box['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None  
    
    return render(request, 'pages/category.html', Box)
    
def PostObj(request, pk) :
    # comment
    post = get_object_or_404(Post, pk = pk)
    form = CommentForm()
    # image of Post
    image = get_object_or_404(Post, pk = pk)
    # Cart
    formCart = CartForm()
    This_Post = Post.objects.get(pk = pk)
    item = This_Post.title
    price = This_Post.price
    

    if request.method == 'POST' :
        form = CommentForm(request.POST, author = request.user, post = post)
        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(request.path)

    if request.method == 'POST' :
        formCart = CartForm(request.POST, user = request.user, item = item, price = price)
        if formCart.is_valid() :
            formCart.save()
            myUser = User.objects.get(username = request.user)
            cart_obj = myUser.cart.all().order_by("-id")
            for i in cart_obj :
                i.price = i.price*i.amount
                i.save()
                break
            return HttpResponseRedirect(request.path)

    This_Obj = Post.objects.get(pk = pk)
    Category = This_Obj.category

    Data = {
        'formCart' : formCart,
        'Obj' : Post.objects.get(pk = pk),
        "post" : post,
        "form" : form,
        'Involve' : Post.objects.filter(category = Category).exclude(pk = pk).order_by('?')[:3],
        'Images' : image,
        'Popular' : Post.objects.filter(category = Category).order_by('?')[:3],
        "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
    }
    AllCategory = [
        'cyberpunk', 'custom', 
        'star_wars', 'ninjago'
    ]
    for i in AllCategory :
        Data[i] = Post.objects.filter(category = i).count()

    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None
        

    return render(request, 'pages/post.html', Data)


