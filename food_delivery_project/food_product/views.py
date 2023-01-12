from django.shortcuts import render,HttpResponse

# Create your views here.
def foodindex(request):
    return HttpResponse("This is food_product page")