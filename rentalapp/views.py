from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from rentalapp.forms import *
from rentalapp.models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def custform(request):
    ct = Custform
    return render(request,'addcust.html',{'cust':ct})


def vehicleform(request):
    vh = Vehiform
    return render(request,'addvehicle.html',{'vehi':vh})


def addcustomer(request):
    if request.method == 'POST':
        ct = Custform(request.POST)
        if ct.is_valid():
            ct.save()
            messages.info(request,'Registration successful')
            return redirect(custform)
    else:
        return redirect(custform)

def custview(request):
    ct = Customer.objects.all()
    return render(request,'custview.html',{'view':ct})

def viewinventory(request):
    ve = Vehicle.objects.all()
    return render(request,'vehicleview.html',{'view':ve})


def bookingform(request):
    bf = Rentalfrom
    return render(request,'rentalbook.html',{'rent':bf})



def addrental(request):
    if request.method == 'POST':
        re = Rentalfrom(request.POST)
        ve_id = request.POST['vehicle_type']
        if re.is_valid():
            ve = Vehicle.objects.get(id=ve_id)
            if ve.inventory>0:
                re.save()
                ve.inventory = ve.inventory - 1
                ve.save()
                messages.info(request,ve.vehicle_type+' '+'Booking successful')
                return redirect('bookingform')
            else:    
                messages.info(request,ve.vehicle_type+' '+'is not available for booking')
                return redirect('bookingform')
    else:
        return redirect(custform) 

def bookview(request):
    rb = RentalBooking.objects.all()
    return render(request,'bookview.html',{'view':rb})
                

def rtn(request,id):
    rb = RentalBooking.objects.get(id=id)
    return render(request,'returndate.html',{'rent':rb})

def update(request,id):
    if request.method == "POST":
        rtn = request.POST['rtndate']
        rb = RentalBooking.objects.get(id=id)
        rb.return_date = rtn
        rb.save()
        return redirect(bookview)
        
             