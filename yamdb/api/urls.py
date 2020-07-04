from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    GenreViewSet,
    TitleViewSet,
    UsersViewSet,
    UserMeViewSet,
    ReviewViewSet,
    CommentViewSet
)    
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
    
router = DefaultRouter()
router.register('categories', CategoryViewSet, basename="category")
router.register("genres", GenreViewSet, basename="genre")
router.register("titles", TitleViewSet, basename="title") 
#router.register("users/me", UserMeViewSet, basename="me")
router.register("users", UsersViewSet, basename="users")
router.register(r'titles/(?P<title_id>[0-9]+)/reviews', ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments', CommentViewSet, basename='coomments')

urlpatterns = [
    path("users/me/", UserMeViewSet.as_view(), name="me"),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]
