from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from Client.models import Client
from Client.serializers import ClientSerializer
from Client.permissions import ClientPermission
from Event.models import Event


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, ClientPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['last_name', 'email']
    search_fields = ['last_name', 'email']

    def get_queryset(self):
        current_user = self.request.user
        if current_user.groups.filter(name='sales').exists() is True:
            return Client.objects.filter(sales_contact=current_user)

        elif current_user.groups.filter(name='support').exists() is True:
            events = Event.objects.filter(support_contact=current_user)
            clients_queryset = events.values_list('client', flat=True).distinct()
            return Client.objects.filter(id__in=clients_queryset)

    def perform_create(self, serializer):
        current_user = self.request.user
        additional_data = {'sales_contact': current_user}
        serializer.save(**additional_data)
