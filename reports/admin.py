from django.contrib import admin
from django.contrib.auth import models
from reports.models import Visit
 
class VisitAdmin(admin.ModelAdmin):
    list_display = ("user", "visit_counter","last_visit")

# Register your models here.
admin.site.register(Visit, VisitAdmin)