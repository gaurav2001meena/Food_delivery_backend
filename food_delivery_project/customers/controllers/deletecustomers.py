from rest_framework.decorators import api_view
from rest_framework.response import Response
from customers.models import Customers
import json


@api_view(['DELETE'])

def deletecustomers(request):
    data = json.loads(request.body)
    email = data['email']

    if Customers.objects.filter(email = email).exists():
        deldata = Customers.objects.get(email=email)
        deldata.delete()
        return Response({"Message" : "Customer deleted successfully"})  
    else:
        return Response({"message" : "Kuch to gadbad hai daya!!!!" , "error" : "no credentials found"})
    