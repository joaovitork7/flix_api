from rest_framework import permissions


class GenrePermissionsClass(permissions.BasePermission):
    def has_permission(self, request, view):
        # logica da permissão
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')
        if request.method == 'POST':
            request.user.has_perm('genres.add_genre')
        if request.method in ['PATH', 'PUT']:
            return request.user.has_perm('genres.changes_genre')
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')

        return False
