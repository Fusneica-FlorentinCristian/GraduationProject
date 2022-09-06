from rest_framework.permissions import BasePermission


class IsTenant(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.isTenant)


class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.isAdministrator)
