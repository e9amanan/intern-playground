from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    custom permission 
    """

    def has_object_permission(self,request,view,obj):
        return obj.owner == request.user