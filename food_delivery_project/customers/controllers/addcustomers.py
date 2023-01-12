from rest_framework.decorators import api_view 
from rest_framework.response import Response
from customers.models import Customers
import json



@api_view(['POST'])

def addcustomers(request):
    data = json.loads(request.body)
    first_name = data['first_name']
    last_name = data['last_name']
    phone_number = data['phone_number']
    email = data['email']
    orders = data['orders']
   
    try : 
     cusdata = Customers.objects.create(first_name = first_name , last_name = last_name , phone_number = phone_number ,email = email , orders = orders)
     cusdata.save()
     return Response({"message" : "User Added Successfully"})

    except Exception as e:
        return Response({"message":"kuch to gadbad hai daya !!!","error":str(e)}) 