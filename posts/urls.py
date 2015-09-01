from django.conf.urls import patterns, include, url
from posts import views

__author__ = 'Chus'

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>[0-9]+)$', views.PostView.as_view(), name='post_detail'),
    url(r'^blogs$', views.BlogsView.as_view(), name='blogs'),
    url(r'^blogs/(?P<username>\w+)', views.BlogView.as_view(), name='blog_detail'),
)