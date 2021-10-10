from django.db import models
from clients.models import Client

from django.urls import reverse

class Payment(models.Model):
    client = models.ForeignKey(Client, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.client.client + ' - ' + str(self.amount)

    class Meta:
        ordering = ['-date']
    
    def get_absolute_url(self):
        return reverse('payments:payment_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('payments:payment_update', kwargs={'pk': self.pk})
    
   
    








    