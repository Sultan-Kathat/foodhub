from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Menu, Category, Restaurant
from reports.models import Visit

import datetime

# Create your views here.

def menu(request, name_fp):

    if not User.objects.filter(username=name_fp).exists():
        return HttpResponse("Restaurant Does Not Exist")

    user = User.objects.get(username=name_fp)
    username = user.username
    restaurant_name = user.restaurant.get()

    categories = Category.objects.filter(rest_category = restaurant_name,).order_by("priority")
    


    categorydetails={}

    # sample_dict = {
    #     "biryani":"chicken,mutton",
    #     "salads":"veg cucumber etc"
    # }
    for category in categories:
        if category.menu_items.all().count()>0: # check if the category have any item in it 
            #print(f"{category.category_name}:  {category.menu_items.all()}")
            for item in category.menu_items.all(): # calling all the item in category using related name and if they have stock/available
                if item.stock==True:
                    categorydetails[category.category_name] = category.description
                    break
    #     else:
    #         print(category)
    # print(categories_active)


    #menu_items = user.menu_items.all()
    menu_items = Menu.objects.filter(rest_id = user, stock = True ).order_by("id")
    #print(restaurant_name.rest_name)


    # if not request.user.is_authenticated:
    #     return HttpResponse("Restaurant Does Not Exist")

    # visitor counter loop
    # visit_counter(name_fp)   
    if not Visit.objects.filter(user = user).exists(): 
        v = Visit(
            visit_counter = 0,
            user = user,
            #last_visit = datetime.now()
            )
        v.save()
    else:
        
        v = Visit.objects.get(user = user)
        #print(v.visit_counter)
        #Visit.objects.filter(user = user).update(visit_counter = current_visit+1)
        v.visit_counter = v.visit_counter +1
        v.save()

    #print(request.user.get_username())

    return render(request, 'menu/menu.html',{
        "name_fp": name_fp,
        "restaurant_name" : restaurant_name,

        "categories": categories,
        "menu_items": menu_items,
        # "sample_dict":sample_dict
        #"menu":menu,
        "categorydetails":categorydetails,
     

    })


def visit_counter():
    pass


def index(request):
    return render(request, "menu/index.html")


def index_anystring(request, anystring):
    return render(request, "menu/index.html")