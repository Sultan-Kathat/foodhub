from django.db import models
from django.contrib.auth.models import User
from reportlab.lib.colors import Blacker



# Create your models here.
class Restaurant(models.Model):
    rest_name= models.CharField(max_length=64)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurant", null=True)
    address_1 = models.CharField(max_length=64, blank=True)
    address_2 = models.CharField(max_length=64, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    city = models.CharField(max_length=64, blank=True)
    state=models.CharField(max_length=64, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return f"{self.rest_name}"

class Category(models.Model):
    category_name = models.CharField(max_length=64)
    rest_category = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="category",null=True)
    priority = models.SmallIntegerField(default=1000)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category_name}"

class Menu(models.Model):
    item_name = models.CharField(max_length=128)
    price_tag = models.CharField(max_length=16, blank=True)
    price= models.IntegerField()
    price_tag1 = models.CharField(max_length=16, blank=True)
    price1= models.IntegerField(blank=True,null=True)
    price_tag2 = models.CharField(max_length=16,blank=True)
    price2= models.IntegerField(blank=True,null=True)
    food_type = models.CharField(max_length=10, blank=True, )
    ingredient = models.TextField(blank=True)
    stock = models.BooleanField()
    quantity = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="menu_items", null=True)
    rest_id =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="menu_items", null=True)
    
    def __str__(self):
        return f"{self.item_name},Price: {self.price}, stock: {self.stock}"


