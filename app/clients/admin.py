from django.contrib import admin
from .models import Client, Gender, License, Location

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "client_id",
        "name",
        "annual_venue_fee",
        "annual_venue_fee_paid",
        "paid",
        "license",
    ]


admin.site.register(Gender)
admin.site.register(Location)
admin.site.register(License)
