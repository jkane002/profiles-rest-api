from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    # gets called every time a request is called
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # uses safe methods that don't edit data, others can view though
        if request.method in permissions.SAFE_METHODS:
            return True

        # if current user has the same id
        return obj.id == request.user.id
