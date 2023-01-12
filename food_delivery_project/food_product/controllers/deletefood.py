from rest_framework.decorators import api_view
from rest_framework.response import Response
from food_product.models import Food
import json


@api_view(['DELETE'])

def deletefood(request):

    data = json.loads(request.body)
    fid = data['fid']

    if Food.objects.filter(fid = fid).exists():
        deldata = Food.objects.get(fid=fid)
        deldata.delete()
        return Response({"Message" : "Food deleted successfully"})
    
    else:
        return Response({"message" : "Kuch to gadbad hai daya!!!!" , "error" : "no credentials found"})
    