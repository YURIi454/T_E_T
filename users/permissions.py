from rest_framework.permissions import BasePermission


class OwnerOrReadOnlyPerm(BasePermission):
    """ Доступ всем пользователям. """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user


class OwnerOnlyPerm(BasePermission):
    """ Доступ только владельцу. """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
