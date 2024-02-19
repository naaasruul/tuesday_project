from django.db import models

# Create your models here.

class Client(models.Model):
    ClientID=models.CharField(max_length=4, primary_key=True)
    Clientname=models.TextField(max_length=50)
    Clientphone=models.CharField(max_length=20)
    Gender=models.CharField(max_length=5)

class Car(models.Model):
    CarPlate=models.CharField(max_length=10, primary_key=True)
    CarType=models.TextField(max_length=30)
    Capacity=models.PositiveIntegerField(null=True , blank=True)

class Rental_Record(models.Model):
    ClientID=models.ForeignKey(Client,on_delete = models.CASCADE)
    CarPlate=models.ForeignKey(Car,on_delete = models.CASCADE)
    TotalPaid=models.PositiveIntegerField(null=True , blank=True)
    Startdate=models.DateTimeField(null=True , blank=True)
    returndate=models.DateTimeField(null=True,blank=True)