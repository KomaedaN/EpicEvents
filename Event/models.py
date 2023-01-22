from django.db import models
from Client.models import Client
from User.models import User
from Contract.models import Contract


class EventStatus(models.Model):
    status = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Event(models.Model):
    client = models.ForeignKey(to=Client, on_delete=models.PROTECT)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    event_status = models.ForeignKey(to=EventStatus, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attendees = models.IntegerField()
    event_date = models.DateField()
    notes = models.TextField(null=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.PROTECT)
