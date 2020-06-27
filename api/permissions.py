from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperuserPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user      

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_superuser)      




class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return bool(request.user.role == 'admin' or request.user.is_superuser)   
    def has_object_permission(self, request, view, obj):            
        #if request.method == "get":
            #return False    
        if request.user.is_authenticated:
            return bool(request.user.role == 'admin' or request.user.is_superuser)     

class IsAdminOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.role == 'admin' or request.user.is_superuser:
                return True 
                                     