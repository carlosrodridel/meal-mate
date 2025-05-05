from rest_framework import permissions


class IsAdminOrSelf(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow anyone to create
        if view.action == "create":
            return True
        # List and destroy only by admin
        if view.action in ["list", "destroy"]:
            return request.user and request.user.is_staff
        # For retrieve, update, partial_update: must be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Retrieve/update: admin or the user themselves
        if view.action in ["retrieve", "update", "partial_update"]:
            return request.user.is_staff or obj == request.user
        # Destroy: only admin
        if view.action == "destroy":
            return request.user.is_staff
        return False
