from django.conf.urls import patterns, include, url
from posts import views

__author__ = 'Chus'

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^blogs/(?P<username>\w+)/(?P<pk>[0-9]+)$', views.PostView.as_view(), name='post_detail'),
    url(r'^blogs$', views.BlogsView.as_view(), name='blogs'),
    url(r'^blogs/(?P<username>\w+)', views.BlogView.as_view(), name='blog_detail'),
    url(r'^new-post', views.CreatePostView.as_view(), name='new_post'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^singup/$', views.SignupView.as_view(), name='signup'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),

)