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
    UserMeViewSet
)    
from rest_framework.authtoken import views
from rest_framework.urlpatterns import format_suffix_patterns
    
router = DefaultRouter()
router.register('categories', CategoryViewSet, basename="category")
#router.register('categories/<slug>', CategoryViewSet.as_view({'delete': 'destroy'})), basename="category")
#router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments") 
router.register("genres", GenreViewSet, basename="genre")
router.register("titles", TitleViewSet, basename="title") 
#router.register("users/me", UserMeViewSet, basename="me")
router.register("users", UsersViewSet, basename="users")


urlpatterns = [
    path("users/me/", UserMeViewSet.as_view(), name="me"),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
]

#urlpatterns = format_suffix_patterns([
    #path("categories/", CategoryViewSet.as_view({'get': 'list'})),
    #path("categories/<slug>/", CategoryViewSet.as_view({'delete': 'destroy'})),
    #path("review/", views.ReviewCreateViewSet.as_view({'post': 'create'})),
    #path("rating/", views.AddStarRatingViewSet.as_view({'post': 'create'})),
    #path('actor/', views.ActorsViewSet.as_view({'get': 'list'})),
    #path('actor/<int:pk>/', views.ActorsViewSet.as_view({'get': 'retrieve'})),
#])