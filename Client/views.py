from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from Client.models import Client
from Client.serializers import ClientSerializer
from Client.permissions import ClientPermission


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerializer

    permission_classes = [IsAuthenticated, ClientPermission]

    def get_queryset(self):
        return Client.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
