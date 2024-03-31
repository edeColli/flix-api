from rest_framework import permissions


class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in ['GET', 'OPTIONS','HEAD']:
            return request.user.has_perm('genres.view_genre')
        elif request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        elif request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')
        elif request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')
        return False