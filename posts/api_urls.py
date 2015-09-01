#encoding:UTF-8
from posts.api import UserViewSet

__author__ = 'Chus'

from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name="user")

urlpatterns = patterns('',
    # api urls
    url(r'', include(router.urls)),

)
