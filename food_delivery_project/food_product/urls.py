from django.contrib import admin
from django.urls import path,include
from food_product import views
from  food_product.controllers.addfood import addfood
from food_product.controllers.deletefood import deletefood

urlpatterns = [
    
    path('' , views.foodindex , name='foodindex'),
    path('addfood' , addfood , name='addfood'),
    path('deletefood', deletefood , name='deletefood')
]