from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from customers.models import Address 
from customers.models import Delivery 
from customers.models import Customers 
from food_product.models import Food 
from customers.models import Order 
from customers.models import Fortest
import json 



@api_view(['POST']) 
 
def fortest(request): 
    data = json.loads(request.body) 
    email = data['email'] 
    email_data = Customers.objects.filter(email=email).get()

    ft = Fortest.objects.get(email=email)
    order = ft.orders
    od = Order.objects.get(email=email_data)
    # q = od.quantity
    # print(q)

    print(order)
    price =0

    for y in order:
        f = Food.objects.get(fid=y)
        p = f.price_data  
        print(f.name ,": ", p) 
        # print("quantity :" , q )
        price = price+p

    print( "total price is : " , price)
    return Response("Jingalala"  ) 
    