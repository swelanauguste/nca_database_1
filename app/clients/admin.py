from django.contrib import admin
from .models import Client, Gender, License, Location

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "client_id",
        "client",
        "annual_venue_fee",
        "annual_venue_fee_paid",
        "paid",
        "slug",
    ]


admin.site.register(Gender)

@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
        list_display = [
        "license",
        "pk",
    ]
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
        list_display = [
        "location",
        "pk",
    ]



