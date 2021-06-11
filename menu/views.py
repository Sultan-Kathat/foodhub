from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Menu, Category, Restaurant

# Create your views here.

def menu(request, name_fp):

    if not User.objects.filter(username=name_fp).exists():
        return HttpResponse("Restaurant Does Not Exist")

    user = User.objects.get(username=name_fp)
    username = user.username
    restaurant_name = user.restaurant.get()

    categories = Category.objects.filter(rest_category = restaurant_name,).order_by("priority")
    
    categories_active = []
    for category in categories:
        if category.menu_items.all().count()>0: # check if the category have any item in it 
            #print(f"{category.category_name}:  {category.menu_items.all()}")
            for item in category.menu_items.all(): # calling all the item in category using related name and if they have stock/available
                if item.stock==True:
                    categories_active.append(category.category_name)
                break
        else:
            print(category)
    print(categories_active)


    #menu_items = user.menu_items.all()
    menu_items = Menu.objects.filter(rest_id = user, stock = True ).order_by("category")
    #print(restaurant_name.rest_name)


    # if not request.user.is_authenticated:
    #     return HttpResponse("Restaurant Does Not Exist")
        

    #print(request.user.get_username())

    return render(request, 'menu/menu.html',{
        "name_fp": name_fp,
        "restaurant_name" : restaurant_name,

        "categories": categories_active,
        "menu_items": menu_items
        #"menu":menu,
     

    })
