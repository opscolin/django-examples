
from django.urls import path
from cmdb.views import borrow_phone, borrow_phone_v2


app_name = 'cmdb'
urlpatterns = [
    path('phone/borrow/<int:pk>/v2/', borrow_phone_v2, name='borrow-phone-v2'),
    path('phone/borrow/<int:pk>/', borrow_phone, name='borrow-phone'),
    
]