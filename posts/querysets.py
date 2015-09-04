#encoding:UTF-8
from django.contrib.auth.models import User

__author__ = 'Chus'

from django.db.models import Q
from posts.models import Post
from wordplease.settings import PUBLIC


class PostQuerySet(object):

    def get_queryset(self):

        user = self.request.user

        if user.is_superuser:
            return Post.objects.all().order_by('-modified_on')
        elif user.is_anonymous():
            return Post.objects.filter(Q(visibility=PUBLIC)).order_by('-modified_on')
        else:
            return Post.objects.filter(Q(owner=user) | Q(visibility=PUBLIC)).order_by('-modified_on')


class BlogQuerySet(object):

    def get_queryset(self):
        return User.objects.all().order_by('username')

