from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Customer(models.Model):
    CustomerName = models.CharField(max_length=20)
    PhoneNumber = models.IntegerField()
    Email = models.EmailField()

    def __str__(self):
        return self.CustomerName

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=15)
    inventory = models.IntegerField()

    def __str__(self):
        return self.vehicle_type


class RentalBooking(models.Model):
    CustomerName = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True)
    rental_date = models.DateField()
    return_date = models.DateField(null=True,blank=True)
    vehicle_type = models.ForeignKey(Vehicle,on_delete=models.CASCADE,blank=True)