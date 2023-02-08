from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True          
        return request.user.id == obj.creator.id
    
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True 
        return bool(request.user and request.user.is_authenticated)
    
# class IsAuthenticated(BasePermission):
#     """
#     Allows access only to authenticated users.
#     """

#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated)