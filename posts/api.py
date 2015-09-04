#encoding:UTF-8

__author__ = 'Chus'

from django.contrib.auth.hashers import make_password
from posts.querysets import PostQuerySet, BlogQuerySet
from django.contrib.auth.models import User
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from posts.permissions import UserPermission, PostPermission
from posts.serializers import UserSerializer, PostSerializer, PostListSerializer, PostDetailSerializer, BlogSerializer


def update_password(serializer):
    password = make_password(serializer.validated_data.get('password'))
    serializer.save(password=password)


# Users
class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    permission_classes = (UserPermission,)
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('username',)
    search_fields = ('username',)
    serializer_class = UserSerializer

    # Password will be encripted after save it
    def perform_create(self, serializer):
        update_password(serializer)

    def perform_update(self, serializer):
        update_password(serializer)



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


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



# Blogs
class BlogViewSet(BlogQuerySet, ListAPIView):
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ('username',)
    search_fields = ('username', 'first_name')
    serializer_class = BlogSerializer



