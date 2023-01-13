from django.db import models
from Client.models import Client
from User.models import User


class Contract(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, related_name='current_client')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    amount = models.FloatField()
    payment_due = models.DateField()
    sales_contact = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
