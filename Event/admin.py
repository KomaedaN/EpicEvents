from django.contrib import admin
from Event.models import EventStatus, Event


admin.site.register(Event)
admin.site.register(EventStatus)

