from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from Event.models import Event
from User.models import User


class EventPermission(BasePermission):

    def has_permission(self, request, view):
        support_team_action = ['list', 'retrieve', 'update']
        sales_team_action = ['create']
        sales_group = User.objects.get(username=request.user).groups.filter(name='sales').exists()
        support_group = User.objects.get(username=request.user).groups.filter(name='support').exists()

        if view.action in support_team_action:
            if support_group is True:
                return True
            else:
                raise PermissionDenied(detail='Only Support team is allowed here')

        elif view.action in sales_team_action:
            if sales_group is True:
                return True
            else:
                raise PermissionDenied(detail='Only Sales team is allowed here')

        elif view.action == 'destroy':
            return False


class EventStatusPermission(BasePermission):
    def has_permission(self, request, view):
        action = ['list', 'create']
        support_group = User.objects.get(username=request.user).groups.filter(name='support').exists()

        if view.action in action:
            if support_group is True:
                return True
            else:
                raise PermissionDenied(detail='Only Support team is allowed here')
