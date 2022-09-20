from django.urls import include, path
from rest_framework import routers

from api.views import (CommentViewSet,
                       FollowViewSet,
                       GroupViewSet,
                       PostViewSet)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comment')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
