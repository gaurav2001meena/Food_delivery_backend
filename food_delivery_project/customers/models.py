from django.db import models
from food_product.models import Food
from django.contrib.postgres.fields import ArrayField , JSONField


class Customers(models.Model):
    first_name = models.CharField( max_length=50 , null=False , default="n/a")
    last_name = models.CharField(max_length=50 , null=False , default="n/a")
    phone_number = models.CharField(max_length=12)
    email = models.EmailField( max_length=254 , unique=True, null=True)
    orders = ArrayField(models.TextField(null=True,default=[]))

    def __str__(self):
        return self.email


class Order(models.Model):
    fid = models.ForeignKey(Food, on_delete=models.CASCADE)
    email = models.ForeignKey(Customers, on_delete=models.CASCADE , null=True)
    first_name = models.CharField(max_length=50)
    food_name = models.CharField( max_length=50 , null=False , default="n/a")
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

    
class Address(models.Model):
    address = models.CharField( max_length=200)
    city = models.CharField(max_length=50)
    pincode = models.IntegerField()
    email = models.ForeignKey(Customers, on_delete=models.CASCADE , null=True )

    def __str__(self):
        return self.address


class Delivery(models.Model):
    email = models.ForeignKey(Customers, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    fid = models.ForeignKey(Food , on_delete=models.CASCADE, null=True)


class Fortest(models.Model):
    name = models.CharField(max_length=50)    
    email= models.EmailField( max_length=254)
    orders = ArrayField(models.CharField(max_length=50)) 
    quantity = ArrayField(models.CharField(max_length=50 , default=[]) , null=True)
