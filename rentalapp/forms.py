from django import forms
from django.forms import models
from .models import *

class Custform(forms.ModelForm):
    class Meta():
        model = Customer
        fields = '__all__'


class Vehiform(forms.ModelForm):
    class Meta():
        model = Vehicle
        fields = '__all__'        


class Rentalfrom(forms.ModelForm):
    class Meta():
        model = RentalBooking
        fields = '__all__'         