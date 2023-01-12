from rest_framework.decorators import api_view 
from rest_framework.response import Response
from food_product.models import Food
import json



@api_view(['POST'])
def addfood(request):
    print("test")
    data = json.loads(request.body)
    fid = data['fid']
    name = data['name']
    category = data['category'],
    price_data = data['price_data']
   
    try : 
     cusdata = Food.objects.create(fid = fid ,name = name , category = category , price_data = price_data  )
     cusdata.save()
     return Response({"message" : "Food Added Successfully"})

    except Exception as e:
        return Response({"message":"kuch to gadbad hai daya !!!","error":str(e)}) 