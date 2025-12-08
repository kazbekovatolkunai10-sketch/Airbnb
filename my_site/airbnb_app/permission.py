from rest_framework.permissions import BasePermission

class CreateProperty(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'host'

class CreateReview(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'quest'
