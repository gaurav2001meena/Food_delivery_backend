from django.contrib import admin
from django.urls import path,include
from customers import views
from customers.controllers.addcustomers import addcustomers
from customers.controllers.orders import orders
from customers.controllers.deletecustomers import deletecustomers
from customers.controllers.addaddress import addaddress
from customers.controllers.delivery import delivery
from customers.controllers.fortest import fortest
urlpatterns = [
    
    path('' , views.index , name='index'),
    path('addcustomers' , addcustomers , name='addcustomers'),
    path('orders' , orders , name='orders'),
    path('deletecustomers' , deletecustomers , name='deletecustomers'),
    path('addaddress' , addaddress , name = 'addaddress'),
    path('delivery' , delivery , name='delivery'),
    path('fortest' , fortest, name='fortest')
    
]