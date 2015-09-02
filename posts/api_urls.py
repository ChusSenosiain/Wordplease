#encoding:UTF-8
from posts.api import UserViewSet, PostViewSet, BlogViewSet

__author__ = 'Chus'

from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name="user")
router.register(r'posts', PostViewSet, base_name="post")
router.register(r'blogs', BlogViewSet, base_name="blog")

urlpatterns = patterns('',
    # api urls
    url(r'', include(router.urls)),

)
