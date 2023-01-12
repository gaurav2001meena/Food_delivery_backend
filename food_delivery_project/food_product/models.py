from django.db import models


#Create your models here.

CATEGORY = (
        ("Breakfast" , "Breakfast"),
        ("Meal" , "Meal"),
        ("Dinner" , "Dinner"),
        ("FastFood" , "FastFood"),
        ("Dessert" , "Dessert")
      )


class Food(models.Model):
    fid = models.CharField(unique=True , max_length=50)
    name = models.CharField( max_length=50 , null=True , default="n/a")
    price_data = models.IntegerField(default=0,null=True)
    category = models.CharField( max_length=50 , choices=CATEGORY,default='Breakfast')

    def __str__(self) :
       return self.name
    

class Test(models.Model):
  pipo = models.CharField(max_length=50 , default="this is a pipo test" , null=True) 