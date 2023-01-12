from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from customers.models import Address 
from customers.models import Delivery 
from customers.models import Customers 
from food_product.models import Food 
from customers.models import Order 
import json 



@api_view(['POST']) 
 
def delivery(request): 
    data = json.loads(request.body) 
    email = data['email'] 
     
    email_data = Customers.objects.filter(email=email).get()
    f = email_data.orders
    fid = f[0]
    fid_data = Food.objects.filter(fid=fid).get()
    add_data = Address.objects.filter(email=email_data).get()
    
    cd = Customers.objects.get(email=email_data)
    ad = Address.objects.get(email=email_data)
    fd = Food.objects.get(fid = fid)
    od = Order.objects.get(email=email_data)
   
    name = cd.first_name
    add = ad.address 
    pincode = ad.pincode
    food = fd.name
    quantity = od.quantity 
    price = od.price
    sp = price/quantity
    
    try : 
     cusdata = Delivery.objects.create(email = email_data, address = add_data  , fid = fid_data)
     cusdata.save()
     return Response({"message" : "Following is the delivery invoice" , "Name : " : name , "Address : " : add , "Pincode : " : pincode , "Item name :" : food ,"Price : " : sp,"Quantity : " : quantity, "Total price : " : price , "Thank you for ordering ..wish u have a great day" : "idk why i am writing this "  })

    except Exception as e:
        return Response({"message":"kuch to gadbad hai daya !!!","error":str(e)}) 