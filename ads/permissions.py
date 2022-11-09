from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwnerSelection(BasePermission):
    message = 'Недостаточно прав'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsOwnerAdOrStaff(BasePermission):
    message = 'Недостаточно прав'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.user.role in [UserRoles.ADMIN, UserRoles.MODERATOR]
