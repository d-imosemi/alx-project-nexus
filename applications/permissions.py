from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Users manage only their own applications.
    Admin can access all.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user
