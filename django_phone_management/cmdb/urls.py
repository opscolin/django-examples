
from django.urls import path
from cmdb.views import borrow_phone


app_name = 'cmdb'
urlpatterns = [
    path('phone/borrow/<int:pk>/', borrow_phone, name='borrow-phone'),
]