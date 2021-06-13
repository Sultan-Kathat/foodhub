from django.db import models
from django.contrib.auth.models import User



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
    
    def __str__(self):
        return f"{self.rest_name}"

class Category(models.Model):
    category_name = models.CharField(max_length=32)
    rest_category = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="category",null=True)
    priority = models.SmallIntegerField(default=1000)

    def __str__(self):
        return f"{self.category_name}"

class Menu(models.Model):
    item_name = models.CharField(max_length=48)
    price= models.IntegerField()
    ingredient = models.TextField(blank=True)
    stock = models.BooleanField()
    quantity = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="menu_items", null=True)
    rest_id =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="menu_items", null=True)
    def __str__(self):
        return f"{self.item_name},Price: {self.price}, stock: {self.stock}"


