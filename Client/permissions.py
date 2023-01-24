from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from Client.models import Client
from User.models import User
from rest_framework.response import Response


class ClientPermission(BasePermission):

    def has_permission(self, request, view):
        view_action = ['list', 'retrieve']
        action = ['create', 'update', 'destroy']
        sales_group = User.objects.get(username=request.user).groups.filter(name='sales').exists()
        support_group = User.objects.get(username=request.user).groups.filter(name='support').exists()

        if view.action in view_action:
            if sales_group is True:
                return True
            elif support_group is True:
                return True

        elif view.action in action:
            if sales_group is True:
                return True
            else:
                raise PermissionDenied(detail='Only Sales team is allowed here')