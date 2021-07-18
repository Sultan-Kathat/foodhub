from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, request, FileResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from menu.models import Restaurant, Category, Menu
from .models import Visit

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponse("Login on admin panel to access this page")

    if not request.user.username == "admin":
        return HttpResponse("Only admin is authorised to visit this page")

    restaurants = Restaurant.objects.all()

    return render(request, "reports/index.html",{
        "restaurants":restaurants
    })


def restaurant_stats(request, rest_id):
    if not request.user.is_authenticated:
        return HttpResponse("Login on admin panel to access this page")

    if not request.user.username == "admin":
        return HttpResponse("Only admin is authorised to visit this page")

    restaurant = Restaurant.objects.get(pk = rest_id)
    user = User.objects.get(username = restaurant.user_name)
    category_count = Category.objects.filter(rest_category = restaurant).count()
    menu_count = Menu.objects.filter(rest_id = user).count()
    visitors = Visit.objects.get(user = user)

    return render(request, "reports/statistics.html",{
        "rest_id":rest_id,
        "restaurant":restaurant,
        "category_count":category_count,
        "menu_count":menu_count,
        "visitors": visitors,

    })