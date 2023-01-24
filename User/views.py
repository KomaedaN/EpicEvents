from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from User.serializers import SignupSerializer
from User.models import User


class SignupViewset(viewsets.ModelViewSet):
    serializer_class = SignupSerializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user)

