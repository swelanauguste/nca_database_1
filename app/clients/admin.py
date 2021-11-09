from django.contrib import admin
from .models import Client, Gender, License, Location, Payment

admin.site.register(Client)
admin.site.register(Gender)
admin.site.register(License)
admin.site.register(Location)
admin.site.register(Payment)