from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from User.serializers import SignupSerializer
from User.models import User, Team


class SignupViewset(viewsets.ModelViewSet):
    serializer_class = SignupSerializer

    def get_queryset(self):
        return User.objects.all()

