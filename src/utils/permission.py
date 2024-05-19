from rest_framework.permissions import SAFE_METHODS, BasePermission


class OrganizerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj.organizer == request.user
