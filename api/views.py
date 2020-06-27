from rest_framework import (
    viewsets, 
    status, 
    permissions, 
    filters,
    generics
)    
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .models import Genre, Title, Category, User
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    UserSerializer
)  
from .permissions import (
    IsSuperuserPermission, 
    IsAuthorOrReadOnlyPermission, 
    IsSuperUser, 
    IsAdminOrReadOnly, 
    IsAdminOrSuperUser
)    
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from .filters import TitleFilter


class CategoryViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [
        IsAdminOrReadOnly
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    def retrieve(self, request, slug):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, slug):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

   
class GenreViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [
        IsAdminOrReadOnly
    ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    
    def retrieve(self, request, slug):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, slug):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UsersViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAdminOrSuperUser
    ]


class UserMeViewSet(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
      

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsSuperUser]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter

