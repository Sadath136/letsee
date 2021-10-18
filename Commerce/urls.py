from django.urls import path
from django.http import HttpResponse
from .views import homepage,su,admin_site
urlpatterns=[
    path('',homepage),
    path('uploaded sucessfully',su,name='home'),
    path('admin_area',admin_site,name='admin_site')
]
