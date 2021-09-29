from django.db import models
from django.urls import reverse


class License(models.Model):
    """
    Model for licenses.
    """

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    """
    Model for location.
    """

    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    """
    Model for clients.
    """

    client_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    dob = models.DateField("date of birth", blank=True, null=True)
    gender = models.ForeignKey(Gender, default=1, on_delete=models.SET_DEFAULT)
    tel = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    location = models.ForeignKey(Location, default=1, on_delete=models.SET_DEFAULT)
    national_insurance_id = models.CharField(max_length=7, blank=True)
    annual_venue_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    annual_venue_fee_paid = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )
    paid = models.BooleanField(default=False)
    license = models.ForeignKey(License, default=1, on_delete=models.SET_DEFAULT)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
