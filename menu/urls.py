from django.urls import path
from . import views

urlpatterns =[
    path('<str:name_fp>', views.menu, name='menu',)
]