#encoding:UTF-8
from wordplease.settings import PUBLIC

__author__ = 'Chus'

from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True
        elif view.action:
            if view.action.lower() == 'create' and not request.user.is_authenticated():
                return True
            elif view.action.lower() in ['retrieve', 'update', 'destroy', 'partial_update']:
                return True

        return False


    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser



class PostPermission(BasePermission):

    def has_permission(self, request, view):
        # solo si el usuario está autenticado puede crear un post
        if view.action and view.action.lower() == 'create':
            return request.user.is_authenticated;

        # Para que pase por has_object_permissions
        return True

    def has_object_permission(self, request, view, obj):
        # si el usuario es admin o el autor del post es el usuario autenticado, le dejo hacer sobre el post
        if request.user.is_superuser or obj.owner == request.user:
            return True
        # para todos los usuarios que no sean propietarios o admin, permito solo ver los publicos
        elif view.action and view.action.lower() == "retrieve":
            return obj.visibility == PUBLIC

        return False
