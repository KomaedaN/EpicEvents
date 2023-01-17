from django.db import models
from Client.models import Client
from User.models import User
from Contract.models import Contract


class Event(models.Model):
    client = models.OneToOneField(to=Client, on_delete=models.CASCADE)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    """event_status = models.ForeignKey(Contract, related_name='status', on_delete=models.CASCADE)"""
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attendees = models.IntegerField()
    event_date = models.DateField()
    notes = models.TextField(null=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
