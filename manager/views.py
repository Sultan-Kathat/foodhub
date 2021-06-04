from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, request
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from menu.models import Restaurant, Category, Menu


# Create your views here.
def index(request):   


    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
        # print("user not found")
        # username = "biryanimoods"
        # password = "123sultan"
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     # Redirect to a success page.
        # #return HttpResponse("User does not exist")

    
   # user = User.objects.get().all()
    if Restaurant.objects.filter(user_name = request.user).exists():
        restaurant_name = Restaurant.objects.get(user_name = request.user)
        user = User.objects.get(username=request.user.username)
        #restaurant_name = user.restaurant.get()

        categories = Category.objects.filter(rest_category = restaurant_name)

        #menu_items = user.menu_items.all()
        menu_items = Menu.objects.filter(rest_id = user ).order_by("category")
        #print(restaurant_name.rest_name)
    else:
        restaurant_name = "No restaurant registered with user"
        return render(request, "manager/index.html", {
            "username": request.user.username,
            "restaurant":restaurant_name,
        })

    

    return render(request, "manager/index.html", {
        "username": request.user.username,
        "restaurant":restaurant_name,
        "categories": categories,
        "menu_items": menu_items


    })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "manager/login.html",{
                "message" : "Invalid Credentials"
            })

    return render(request, "manager/login.html")

def logout_view(request):
    logout(request)

    return render(request, "manager/login.html", {
        "logout_message":"Logged Out"
    })


def edit_menu(request, menu_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))


    if request.method == "POST":
        print(f"Stock value: {request.POST['stock']}")
        return HttpResponseRedirect(reverse("index"))

    menu = Menu.objects.get(pk = menu_id)
    categories = Category.objects.filter(rest_category = Restaurant.objects.get(user_name = request.user))
    rest_id = User.objects.get(username = request.user.username)

    return render(request, "manager/editmenu.html",{
        "menu":menu,
        "categories": categories,
        "rest_id":rest_id,
    })
    