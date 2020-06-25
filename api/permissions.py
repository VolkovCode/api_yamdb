from rest_framework import permissions


class IsSuperuserPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

class IsAuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        #if request.method in permissions.SAFE_METHODS:
            #return True
        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user      

class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_superuser)      

from rest_framework.permissions import BasePermission, SAFE_METHODS


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

class IsAdminOrReadOnlyOne(BasePermission):
    def has_permission(self, request, view):
        
        if request.user.is_authenticated:
            return bool(request.user.role == 'admin' or request.user.is_superuser)                         