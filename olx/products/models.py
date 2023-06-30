from django.db import models

# Create your models here.
class Items(models.Model):
    name=models.CharField(max_length=400)
    price=models.FloatField()
    stock=models.IntegerField()
    desc=models.CharField(max_length=1000)
    image=models.CharField(max_length=400)