from rest_framework.decorators import api_view 
from rest_framework.response import Response
from customers.models import Address
from customers.models import Customers
import json



@api_view(['POST'])

def addaddress(request):
    data = json.loads(request.body)
    address = data['address']
    city = data['city']
    pincode = data['pincode']
    email = data['email']    

    email_data = Customers.objects.filter(email=email).get()  ## instance creating
   
    try : 
     cusdata = Address.objects.create(address = address , city = city , pincode = pincode ,email = email_data)
     cusdata.save()
     return Response({"message" : "Address Added Successfully"})

    except Exception as e:
        return Response({"message":"kuch to gadbad hai daya !!!","error":str(e)}) 