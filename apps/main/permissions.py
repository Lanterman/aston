from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """If owner - everything is allowed, otherwise only reading"""

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user.id == obj.author_id.id
        )
