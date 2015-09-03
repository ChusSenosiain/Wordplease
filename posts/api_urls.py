#encoding:UTF-8
__author__ = 'Chus'

from posts.api import UserViewSet, PostViewSet, BlogViewSet
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name="user")
router.register(r'posts', PostViewSet, base_name="post")


urlpatterns = patterns('',
    # api urls
    url(r'', include(router.urls)),
    url(r'blogs/$', BlogViewSet.as_view()),

)
