#encoding:UTF-8
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.permissions import UserPermission, PostPermission
from posts.serializers import UserSerializer, PostSerializer, PostListSerializer, PostDetailSerializer, BlogSerializer
from wordplease.settings import PUBLIC

__author__ = 'Chus'


class UserViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('username')
    search_fields = ('username')

    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.all()


class PostViewSet(ModelViewSet):

    permission_classes = (PostPermission,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('title', 'updated_date')
    search_fields = ('title', 'content')

    def get_serializer_class(self):
        if self.action:
            if self.action.lower() == 'list':
                return PostListSerializer
            elif self.action.lower() == 'retrieve':
                return PostDetailSerializer

        return PostSerializer

    def get_queryset(self):
        user = self.request.user

        if (user.is_superuser):
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(Q(owner=user) | Q(visibility=PUBLIC))

        return posts


class BlogViewSet(ModelViewSet):

    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('username')
    search_fields = ('username', 'first_name')

    def get_serializer_class(self):
        return BlogSerializer

    def get_queryset(self):
        return User.objects.all()


