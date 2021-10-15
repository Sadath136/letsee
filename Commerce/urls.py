from django.urls import path
from django.http import HttpResponse
from .views import homepage,su
urlpatterns=[
    path('',homepage),
    path('uploaded sucessfully',su,name='home')
]