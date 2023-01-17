from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from Client.models import Client
from User.models import User, Team
from rest_framework.response import Response


class ClientPermission(BasePermission):

    def has_permission(self, request, view):
        action = ['create', 'retrieve', 'list', 'update', 'destroy']
        current_user = User.objects.get(username=request.user).team

        if current_user.team == 'SALES':
            return True

        elif current_user.team == 'ADMIN':
            return True
        else:
            raise PermissionDenied(detail='Only Sales team is allowed here')
