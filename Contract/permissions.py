from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from Client.models import Client
from User.models import User
from rest_framework.response import Response


class ContractPermission(BasePermission):

    def has_permission(self, request, view):
        action = ['list', 'retrieve', 'create', 'update']
        sales_group = User.objects.get(username=request.user).groups.filter(name='sales').exists()

        if view.action in action:
            if sales_group is True:
                return True
            else:
                raise PermissionDenied(detail='Only Sales team is allowed here')

        elif view.action == 'destroy':
            return False
