from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    message = 'This action is restricted to only users registered as farmers.'
    
    def has_object_permission(self, request, obj):
        
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the crop.
        return obj.farmer.user == request.user 