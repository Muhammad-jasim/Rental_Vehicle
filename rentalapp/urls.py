from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('custform',views.custform,name="addcust"),
    path('addcustomer',views.addcustomer,name="addcustomer"),
    path('custview',views.custview,name="custview"),
    path('viewinventory',views.viewinventory,name='viewinventory'),
    path('bookingform',views.bookingform,name='bookingform'),
    path('addrental',views.addrental,name='addrental'),
    path('bookview',views.bookview,name='bookview'),
    path('returndate/<id>',views.rtn,name='returndate'),
    path('update/<id>',views.update,name='update'),

]