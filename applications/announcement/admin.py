from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.contrib import admin
from applications.announcement.models import Announcement


class IsOwner(BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

    # RETRIEVE, UPDATE, DELETE
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user == obj.owner or request.user.is_staff)

admin.site.register(Announcement)
