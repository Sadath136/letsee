from django.contrib import admin
from .models import Collect
class CollectAdmin(admin.ModelAdmin):
    fields = ['name','phone_number','image']
    search_fields = ['name','phone_number','image']
    list_filter = ['name','phone_number','image']
admin.site.register(Collect,CollectAdmin)
