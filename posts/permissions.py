#encoding:UTF-8
__author__ = 'Chus'

from wordplease.settings import PUBLIC
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):

        # superuser is always allowed to do all
        if request.user.is_superuser:
            return True
        elif view.action:
            # Only unauthenticated users can create a user
            if view.action.lower() == 'create' and not request.user.is_authenticated():
                return True
            # Only authenticated users can retrieve, update an destroy an user.
            # The final permission sets by has_object_permission
            elif view.action.lower() in ['retrieve', 'update', 'destroy', 'partial_update']:
                return True

        return False


    def has_object_permission(self, request, view, obj):
        # Returns true if the autenthicated user is the same than the user to update or the the autenthicated is superuser
        return obj == request.user or request.user.is_superuser



class PostPermission(BasePermission):

    def has_permission(self, request, view):
        # Only authenticated users can create a post
        if view.action and view.action.lower() == 'create':
            return request.user.is_authenticated

        # Returns True to handle has_object_permission
        return True

    def has_object_permission(self, request, view, obj):
        # If the user is superuser or the post's owner is the same that the request user, returns true
        if request.user.is_superuser or obj.owner == request.user:
            return True
        # If the user isn't the post's owner, only can retrieve PUBLIC posts
        # WARNING: for list action, the permissions are allowed by the query_set
        elif view.action and view.action.lower() == 'retrieve':
            return obj.visibility == PUBLIC

        return False
