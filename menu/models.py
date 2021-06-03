from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Restaurant(models.Model):
    rest_name= models.CharField(max_length=64)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="restaurant", null=True)
    
    def __str__(self):
        return f"{self.rest_name}"

class Category(models.Model):
    category_name = models.CharField(max_length=32)
    rest_category = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="category",null=True)

    def __str__(self):
        return f"{self.id}: {self.category_name}, Restaurant : {self.rest_category}"

class Menu(models.Model):
    item_name = models.CharField(max_length=48)
    price= models.IntegerField()
    ingredient = models.TextField()
    stock = models.BooleanField()
    quantity = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="menu_items", null=True)
    rest_id =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="menu_items", null=True)
    def __str__(self):
        return f"{self.item_name},Price: {self.price}, stock: {self.stock}"


