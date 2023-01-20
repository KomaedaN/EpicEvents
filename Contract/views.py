from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from Contract.models import Contract
from Client.models import Client
from Contract.serializers import ContractSerializer
from Contract.permissions import ContractPermission


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractPermission]

    def get_queryset(self):
        return Contract.objects.filter(client=self.kwargs['client_pk'], sales_contact=self.request.user)

    def perform_create(self, serializer):
        current_user = self.request.user
        current_client = self.kwargs['client_pk']
        client_id = Client.objects.get(pk=current_client)
        additional_data = {'client': client_id, 'sales_contact': current_user, 'status': True}
        serializer.save(**additional_data)

    def perform_update(self, serializer):
        current_client = self.kwargs['client_pk']
        client_id = Client.objects.get(pk=current_client)
        additional_data = {'client': client_id}
        serializer.save(**additional_data)
