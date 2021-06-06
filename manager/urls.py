from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('editmenu/<int:menu_id>', views.edit_menu, name="edit_menu"),
    path('add/', views.add, name="add"),
    path('category/', views.category, name="category"),
    path('updateprice/<int:item_id>', views.update_price, name="update_price"),
    path('updatestock/<int:item_id>', views.update_stock, name="update_stock"),
    path('deletemenu/<int:menu_id>',views.delete_menu, name="delete_menu" ),
    path('deletecategory/',views.delete_category,name="delete_category"),

]