#encoding:UTF-8
__author__ = 'Chus'

from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Describe si el usuario puede realizasr la accion
        Solo los usuarios no autenticados pueden crear un usuario
        Solo los admin pueden ver el listado de usuarios, y actualizar, eliminar todos los perfiles
        Un usuario solo puede ver su perfil
        Un usuario solo puede actualizar su perfil
        Un usuario solo puede eliminar su perfil
        :param request:
        :param view:
        :return:
        """

        # Si la petición es post, es creación: solo el usuario no autenticado puede crear un usuario
        if view.action.lower() == 'create' and not request.user.is_authenticated():
            return True
        # Si es superusuario le dejamos hacer
        elif request.user.is_superuser:
            return True
        # Si es la vista del detalle, permito: la verficacion se hace en has_object_description
        elif view.action.lower() is ['retrieve', 'update', 'destroy', 'partial_update']:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser