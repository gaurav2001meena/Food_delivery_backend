from rest_framework.decorators import api_view 
from rest_framework.response import Response
from customers.models import Customers
from customers.models import Order
from food_product.models import Food
import json



@api_view(['POST'])

def orders(request):    
    data = json.loads(request.body)
    email = data['email']
    quantity = data['quantity']


    customers_data = Customers.objects.get(email=email)
    food_id = customers_data.orders
    food_id1 = food_id[0]
    food_data = Food.objects.get(fid=food_id1)
    first_name = customers_data.first_name
    food_name = food_data.name
    t = food_data.price_data
    price = quantity*t 
    customers_data = Customers.objects.filter(email=email).get()
    food_data  = Food.objects.filter(fid=food_id1).get()

    try:
        data = Order.objects.create(fid =food_data  ,email=customers_data , first_name = first_name ,food_name=food_name ,quantity=quantity ,price=price)
        data.save()
        return Response({"message" : "Your order is " , "email" : customers_data.email , "first_name" : customers_data.first_name , "food_name" : food_data.name ,"quantity" : quantity ,"price" : price , "have a nice day" : " :) "})

    except Exception as e:
        return Response({"message":"kuch to gadbad hai daya !!!","error":str(e)}) 