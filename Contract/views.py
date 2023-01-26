from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from Contract.models import Contract
from Client.models import Client
from Contract.serializers import ContractSerializer
from Contract.permissions import ContractPermission


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, ContractPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['client__last_name', 'client__email', 'date_created', 'amount']
    search_fields = ['client__last_name', 'client__email', 'date_created', 'amount']

    def get_queryset(self):
        return Contract.objects.filter(sales_contact=self.request.user)

    def perform_create(self, serializer):
        current_user = self.request.user
        additional_data = {'sales_contact': current_user, 'status': True}
        serializer.save(**additional_data)
