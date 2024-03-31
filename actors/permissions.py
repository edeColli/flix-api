from rest_framework import permissions


class ActorPermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in ['GET', 'OPTIONS','HEAD']:
            return request.user.has_perm('actors.view_actor')
        elif request.method == 'POST':
            return request.user.has_perm('actors.add_actor')
        elif request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('actors.change_actor')
        elif request.method == 'DELETE':
            return request.user.has_perm('actors.delete_actor')
        return False