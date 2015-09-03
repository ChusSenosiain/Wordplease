#encoding:UTF-8
__author__ = 'Chus'

from posts.querysets import PostQuerySet
from django.contrib.auth.models import User
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from posts.permissions import UserPermission, PostPermission
from posts.serializers import UserSerializer, PostSerializer, PostListSerializer, PostDetailSerializer, BlogSerializer



# Users
class UserViewSet(ModelViewSet):
    permission_classes = (UserPermission,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('username')
    search_fields = ('username')

    def get_serializer_class(self):
        return UserSerializer

    def get_queryset(self):
        return User.objects.all()

# Posts
class PostViewSet(PostQuerySet, ModelViewSet):

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

# Blogs
class BlogViewSet(ListAPIView):

    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('username')
    search_fields = ('username', 'first_name')

    def get_serializer_class(self):
        return BlogSerializer

    def get_queryset(self):
        return User.objects.all()


