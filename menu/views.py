from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Menu, Category, Restaurant

# Create your views here.
dish_name=["Chicken Biryani", "Mutton Biryani", " Chicken Biryani (Boneless)", "Mutton Biryani(Boneless)", "Egg Biryani",  ]

price=["250.00", "300.00", "350.00","300.00", "350.00", ],

ingredients=[
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",
"Lorem ipsum dolor sit amet, consectetur adipiscing elit",

],
menu={}








def menu(request, name_fp):

    if not User.objects.filter(username=name_fp).exists():
        return HttpResponse("Restaurant Does Not Exist")
    
    user = User.objects.get(username=name_fp)
    username = user.username
    restaurant_name = user.restaurant.get()

    categories = Category.objects.filter(rest_category = restaurant_name)

    #menu_items = user.menu_items.all()
    menu_items = Menu.objects.filter(rest_id = user ).order_by("category")
    print(restaurant_name.rest_name)


    # if not request.user.is_authenticated:
    #     return HttpResponse("Restaurant Does Not Exist")
        

    #print(request.user.get_username())

    return render(request, 'menu/menu.html',{
        "name_fp": name_fp,
        "restaurant_name" : restaurant_name,
        "categories": categories,
        "menu_items": menu_items
        #"menu":menu,
     

    })
