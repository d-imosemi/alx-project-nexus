# jobs/permissions.py
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(request.user, 'role', None) == 'admin' or request.user.is_staff

class IsEmployerOrAdminForJob(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE methods allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        if getattr(request.user, 'role', None) == 'admin' or request.user.is_staff:
            return True
        return obj.posted_by_id == request.user.id and getattr(request.user, 'role', None) == 'employer'


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("GET",):
            return True
        if request.user.is_staff:
            return True
        return obj.posted_by == request.user
    



class IsAdminUser(permissions.BasePermission):
    """
    Allows access only to admin users (is_staff=True).
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)

    