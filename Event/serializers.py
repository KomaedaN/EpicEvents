from rest_framework.serializers import ModelSerializer
from Event.models import EventStatus, Event
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class EventStatusSerializer(ModelSerializer):
    class Meta:
        model = EventStatus
        fields = '__all__'
        read_only_fields = ['id', 'date_created', 'date_updated']


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ['id', 'date_created', 'date_updated', 'client']
