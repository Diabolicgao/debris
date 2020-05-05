from django.shortcuts import render
from data.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchVector
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.

def Home(request) :
    Data_List = Post.objects.all().order_by('-time')
    query = request.GET.get('search')
    if query :
        Data_List = Post.objects.filter(title__icontains = query)    
        url = '/category/all/?search={}'.format(query)
        return HttpResponseRedirect(url)
    Data = {
        # Post Tab 
            "PostTab" : Post.objects.exclude(category = 'custom').order_by('-time')[:4],
        # /Post Tab

        # Event
            "Event" : Event.objects.filter(category= 'event').order_by('-time')[:1],
            "Marginal" : Event.objects.filter(category= 'event').order_by('-time')[1:3],
        # /Event

        # Post Body/ Custom/ Cyber Punk/ Orther
            "PostBody" : Post.objects.all().exclude(Q(category = 'custom')).order_by('-time')[:6],
            "Custom" : Post.objects.filter(category = 'custom').order_by('?')[:3],
            "CyberPunk" : Post.objects.filter(category = 'cyberpunk').order_by('-time')[:3],
            "Other" : Post.objects.filter(Q(category = 'fantasy') | Q(category = 'star_wars')).order_by('-time')[:3],
        # /Post Body/ Custom/ Cyber Punk/ Orther

        # Post Random
            "All" : Post.objects.filter(
                        Q(category = 'vehicle') | 
                        Q(category = 'fantasy') |
                        Q(category = 'technic')
                    )
                    .order_by('?')[:3],

            "All2" : Post.objects.filter(
                        Q(category = 'item') |
                        Q(category = 'dragon') |
                        Q(category = 'brick')
                    )
                    .order_by('?')[:3],

            "All3" : Post.objects.filter(
                        Q(category = 'star_wars') |
                        Q(category = 'cyberpunk') |
                        Q(category = 'custom')
                    )
                    .order_by('?')[:3],
        # /Post Random

        # Ig
            "IG" : Post.objects.all().order_by('?')[:6],
        # /Ig
        
        # Count Category 
            "Count_Custom" : Post.objects.filter(category = 'custom').count(),
            "Count_Star_Wars" : Post.objects.filter(category = 'star_wars').count(),
            "Count_Ninjago" : Post.objects.filter(category = 'ninjago').count(),
            "Count_CyberPunk" : Post.objects.filter(category = 'cyberpunk').count(),
        # /Count Category

        # Sale 
            "Sale" : Post.objects.all().order_by('time')[:5],
        # /Sale

        # Notify
            "Notify" : Event.objects.filter(category= 'notify').order_by('-time')[:3],
        # /Notify

        # Random
            "Rd" : Post.objects.exclude(category = 'custom').order_by('?')[:4],
        # /Random
    }   

    try:
        myUser = User.objects.get(username = request.user)
        count_cart = myUser.cart.all().count()
        Data['count_cart'] = count_cart
    except User.DoesNotExist:
        myUser = None
        
    return render(request, "pages/home.html", Data)

def About(request) :
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
    return render(request, "pages/about.html", Data)

def Author(request) :
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
    return render(request, "pages/author.html", Data)

def Blank(request) :
    return render(request, "pages/blank.html")

def Blog(request) :
    return render(request, "pages/post.html")

def Contact(request) :
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
    return render(request, "pages/contact.html", Data)

    
