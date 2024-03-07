
from django.urls import path
from helloworld.views import hello

urlpatterns = [
    path('', hello, name='hello-world'),
]
