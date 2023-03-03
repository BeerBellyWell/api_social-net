from api.views import (
    PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
)

from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet, basename='comments'
)
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
