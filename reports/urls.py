from django.urls import path
from . import views


urlpatterns=[
    path("", views.index, name="reports_index"),
    path("<int:rest_id>", views.restaurant_stats, name="restaurant_stats"),
]