from rest_framework import permissions


class IsOwnerUserOrListOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permission.SAFE_METHODE:
            return True
        return obj.username == request.user
