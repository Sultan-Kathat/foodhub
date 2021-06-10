from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, request, FileResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from menu.models import Restaurant, Category, Menu

from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import code39, code128, code93, createBarcodeDrawing
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics import renderPDF
from reportlab.graphics.shapes import Drawing 
from reportlab.lib.units import mm
from reportlab.lib.colors import pink, black, red, blue, green

import io



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
    #print('here')

    # if request.method=="POST":
    #     print("hello")
    #     print(request.POST["price"])

    
   # user = User.objects.get().all()
    if Restaurant.objects.filter(user_name = request.user).exists():
        restaurant_name = Restaurant.objects.get(user_name = request.user)

        user = User.objects.get(username=request.user.username)
 

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
        # print(f"Item_name: {request.POST['item_name']}")
        # print(f"Category ID: {request.POST['category']}")
        Menu.objects.filter(pk=menu_id).update(
            item_name=request.POST["item_name"],
            price = request.POST["price"],
            ingredient = request.POST["ingredient"],
            stock = request.POST["stock"],            
            category = Category.objects.get(pk = request.POST["category"]),
            rest_id = User.objects.get(username = request.user.username)
            )
        return HttpResponseRedirect(reverse("index"))
    
    #restaurant name to display on the top
    restaurant = Restaurant.objects.get(user_name = User.objects.get(username = request.user.username))

    menu = Menu.objects.get(pk = menu_id)
    categories = Category.objects.filter(rest_category = Restaurant.objects.get(user_name = request.user))
    rest_id = User.objects.get(username = request.user.username)

    return render(request, "manager/editmenu.html",{
        "restaurant":restaurant.rest_name,
        "username":request.user.username,

        "menu":menu,
        "categories": categories,
        "rest_id":rest_id,

    })


# Add new menu item in catalogue

def add(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    message = ""
    if request.method =="POST":
        if Menu.objects.filter(item_name = request.POST["item_name"]).exists():
            message = "Item already exists in Menu"
        else:
            m = Menu(
            item_name=request.POST["item_name"],
            price = int(request.POST["price"]),
            ingredient = request.POST["ingredient"],
            stock = request.POST["stock"],            
            category = Category.objects.get(pk = request.POST["category"]),
            rest_id = User.objects.get(username = request.user.username)
            )
            m.save()
            return HttpResponseRedirect(reverse("index"))

    #restaurant name to display on the top
    restaurant = Restaurant.objects.get(user_name = User.objects.get(username = request.user.username))

    # laod the categories and restaurant to the form select option
    categories = Category.objects.filter(rest_category = Restaurant.objects.get(user_name = request.user))
    rest_id = User.objects.get(username = request.user.username)


    return render(request, "manager/add.html",{
        "restaurant":restaurant,
        "username": request.user.username,

        "categories": categories,
        "rest_id":rest_id,
        "message": message,
    } )


def category(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    restaurant = Restaurant.objects.get(user_name = User.objects.get(username = request.user.username))
    message=""
    if request.method=="POST":
        new_category = request.POST["category"]
        #print(f"new vategory: {new_category}")
        if Category.objects.filter(category_name = new_category).exists():
            message = "Category already exists in Menu"
        else:        
            c = Category(
                category_name = new_category, 
                rest_category = Restaurant.objects.get(user_name = request.user)
                )
            c.save()
            return HttpResponseRedirect(reverse("index"))

      

    return render(request, "manager/category.html",{
        "restaurant": restaurant,
        "username": request.user.username,
        "message":message,
        # "categories":categories,
    })

    
def update_price(request, item_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.method=="POST":
        Menu.objects.filter(id = item_id).update(price = int(request.POST["price"]))
        # print(item_id)
        # print(request.POST["price"])

    return HttpResponseRedirect(reverse("index"))

def update_stock(request, item_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if request.method=="POST":
        Menu.objects.filter(id = item_id).update(stock = request.POST["stock"])
        # print(item_id)
        # print(request.POST["stock"])

    return HttpResponseRedirect(reverse("index"))


def delete_menu(request, menu_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))


    if Menu.objects.filter(id = menu_id).exists():
        Menu.objects.filter(id = menu_id).delete()
    return HttpResponseRedirect(reverse("index"))

def delete_category(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    message=""

    if request.method=="POST":  
        category_id = request.POST["category_id"]
        if Category.objects.filter(id = category_id).exists():
            Category.objects.filter(id = category_id).delete()
            message = "Category deleted"
        


    restaurant= Restaurant.objects.get(user_name = request.user)
    categories = Category.objects.filter(rest_category = Restaurant.objects.get(user_name = request.user)) 

    return render(request, "manager/deletecategory.html",{
        "restaurant":restaurant,
        "categories":categories,
        "message":message,
    })

def qrcode(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    message=""

    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    p.setPageSize((105*mm, 148*mm))

    # draw rectangle
    p.setFillColorCMYK(0,0.6,0.8,0)
    #p.setFillColor(black)
    #p.setFillColorRGB(14,25,12)
    #canvas.rect(x, y, width, height, stroke=1, fill=0) 
    p.rect(0*mm, 133*mm,105*mm, 15*mm,stroke=0, fill=1)

    #print name of restaurant on the PDF
    r = Restaurant.objects.get(user_name= request.user)
    rest_name = r.rest_name
    font_size = 20
    #Helvetica
    p.setFont('Helvetica-Bold', font_size)
    p.setFillColorCMYK(0,0,0,0.1)
    #canvas.drawCentredString will draw string keeping the x,y in center of the string
    p.drawCentredString(52.5*mm, 138.5*mm, rest_name.upper())
    #MENU
    p.setFont('Helvetica-Bold', 30)
    p.setFillColorCMYK(0,1,1,0)
    p.drawCentredString(52.5*mm, 120*mm, "MENU")
    #Scan the code
    p.setFont('Helvetica-Bold', 20)
    p.setFillColorCMYK(0.02,0.86,0.67,0.02)
    p.rect(22*mm, 105*mm,61*mm, 9*mm,stroke=0, fill=1)
    p.setFillColorCMYK(0,0,0,0.1)
    p.drawCentredString(52.5*mm, 107*mm, "SCAN THE CODE")

    #Helvetica-Oblique:
    p.setFont('Courier-Oblique', 14)
    p.setFillColor(black)
    p.drawCentredString(52.5*mm, 15*mm, f"visit: ZuBu.in/menu/{request.user.username}")


 


    #draw a QR code
    qr_code = qr.QrCodeWidget(f"visit: ZuBu.in/menu/{request.user.username}")
    bounds = qr_code.getBounds()
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    d = Drawing(85*mm, 85*mm,transform=[85*mm/width,0,0,85*mm/height,0,0])
    # transform=[45./width,0,0,45./height,0,0]
    d.add(qr_code)
    renderPDF.draw(d, p, 10*mm, 20*mm)

    p.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="qrcode.pdf")









    
        
