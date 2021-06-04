from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models
from menu.models import Menu, Category, Restaurant

class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "item_name", "price", "stock","category", "rest_id")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","category_name","rest_category")

# Register your models here.
admin.site.register(Menu, MenuAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Restaurant)


