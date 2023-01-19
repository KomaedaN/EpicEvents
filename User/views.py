from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from User.serializers import SignupSerializer
from User.models import User, Team


class SignupViewset(viewsets.ModelViewSet):
    serializer_class = SignupSerializer

    def get_queryset(self):
        return User.objects.all()

    def get_serializer(self, *args, **kwargs):
        if self.request.method in ['PUT']:
            kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)

    def perform_update(self, serializer):
        new_group = serializer.validated_data.get('group')
        user = User.objects.get(pk=self.kwargs['pk'])
        if new_group == 'sales':
            sales_group, created = Group.objects.get_or_create(name='sales')
            user.groups.clear()
            user.groups.add(sales_group)
            user.save()
        elif new_group == 'support':
            support_group, created = Group.objects.get_or_create(name='support')
            user.groups.clear()
            user.groups.add(support_group)
            user.save()
        """print(user.groups.filter(name='support').exists())"""
