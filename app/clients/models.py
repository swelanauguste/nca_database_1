from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import Sum


class License(models.Model):
    """
    Model for licenses.
    """

    license = models.CharField(max_length=50, unique=True)
    vending_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    detail = models.TextField(blank=True)

    class Meta:
        ordering = ["license"]

    def __str__(self):
        return self.license


class Location(models.Model):
    """
    Model for location.
    """

    location = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.location


class Gender(models.Model):
    gender = models.CharField(max_length=6, unique=True)

    class Meta:
        ordering = ['gender']

    def __str__(self):
        return self.gender


class Client(models.Model):
    """
    Model for clients.
    """

    client_id = models.CharField(max_length=10)
    slug = models.SlugField(max_length=10, unique=True, blank=True, null=True)
    client = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    dob = models.DateField("date of birth", blank=True, null=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    tel = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    national_insurance_id = models.CharField("NIC", max_length=7, blank=True)
    license = models.ManyToManyField(License, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.client_id)
        super(Client, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("clients:detail", kwargs={"slug": self.slug})

    def get_absolute_update_url(self):
        return reverse("clients:update", kwargs={"slug": self.slug})

    def get_client_payment(self):
        return self.payments.all()

    def get_total_payments(self):
        return self.payments.all().aggregate(Sum('amount'))['amount__sum']   

    class Meta:
        ordering = ["client"]

    def __str__(self):
        return self.client


class Payment(models.Model):
    client = models.ForeignKey(
        Client, related_name="payments", on_delete=models.CASCADE
    )
    # balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    
    
    def get_vending_fee(self):
        self.client.license
    
    # def save(self, *args, **kwargs):
    #     self.balance = self.get_vending_fee - self.amount
    #     super(Client, self).save(*args, **kwargs)


    def __str__(self):
        return self.client.client + " - " + "XCD$" + str(self.amount)

    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self):
        return reverse("payments:payment-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("payments:payment-update", kwargs={"pk": self.pk})
