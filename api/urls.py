from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentViewSet)
router.register('follow', views.FollowViewSet)
router.register('group', views.GroupViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
