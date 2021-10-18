from django.db import models
from django.db.models import Model
class Collect(models.Model):
    name=models.CharField(max_length=300,null=False,blank=False)
    phone_number=models.CharField(max_length=10,null=False,blank=False,unique=True)
    image=models.FileField(null=False,max_length=400)
    def __str__(self):
        return self.name


