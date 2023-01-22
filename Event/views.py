from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from Event.models import Event, EventStatus
from Event.serializers import EventSerializer, EventStatusSerializer
from Event.permissions import EventPermission, EventStatusPermission

from Client.models import Client
from Contract.models import Contract
from User.models import User


class EventViewset(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, EventPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['client__last_name', 'client__email', 'event_date']
    search_fields = ['client__last_name', 'client__email', 'event_date']

    def get_queryset(self):
        return Event.objects.filter(contract=self.kwargs['contract_pk'], support_contact=self.request.user)

    def perform_create(self, serializer):
        support_contact_entry = serializer.validated_data.get('support_contact')
        support_group = User.objects.get(username=support_contact_entry).groups.filter(name='support').exists()
        if support_group is True:
            client_id = Client.objects.get(pk=self.kwargs['client_pk'])
            contract_id = Contract.objects.get(pk=self.kwargs['contract_pk'])
            additional_data = {'client': client_id, 'contract': contract_id}
            serializer.save(**additional_data)
        else:
            raise ValidationError({'Support contact': "You can't assign this User as 'support_contact'"})

    def perform_update(self, serializer):
        support_contact_entry = serializer.validated_data.get('support_contact')
        support_group = User.objects.get(username=support_contact_entry).groups.filter(name='support').exists()
        if support_group is True:
            client_id = Client.objects.get(pk=self.kwargs['client_pk'])
            contract_id = Contract.objects.get(pk=self.kwargs['contract_pk'])
            additional_data = {'client': client_id, 'contract': contract_id}
            serializer.save(**additional_data)

        else:
            raise ValidationError({'Support contact': "You can't assign this User as 'support_contact'"})


class EventStatusViewset(ModelViewSet):
    serializer_class = EventStatusSerializer
    permission_classes = [IsAuthenticated, EventStatusPermission]

    def get_queryset(self):
        return EventStatus.objects.all()

