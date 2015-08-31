from django.conf.urls import patterns, include, url
from posts import views

__author__ = 'Chus'

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^post/(?P<pk>[0-9]+)$', views.PostView.as_view(), name='post_detail'),
)