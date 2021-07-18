from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField, PositiveBigIntegerField
from menu.models import Restaurant, Menu, Category

# Create your models here.
class Visit(models.Model):
    visit_counter = PositiveBigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visits")
    last_visit = DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.user} is visited {self.visit_counter} times"