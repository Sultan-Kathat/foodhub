from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('editmenu/<int:menu_id>', views.edit_menu, name="edit_menu"),
    path('add/', views.add, name="add"),

]