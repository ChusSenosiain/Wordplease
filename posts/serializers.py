#encoding=UTF-8
__author__ = 'Chus'

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from posts.models import Post, Category

# User Serializers
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ('id')
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


# Blog Serializers
class BlogSerializer(ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='blog_detail', lookup_field='username')

    class Meta:
        model = User
        fields = ('username', 'url')



# Category Serializers
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')



# Post Serializers
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'url', 'summary', 'content', 'categories')


class PostDetailSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)
    categories = CategorySerializer(many=True)
    class Meta:
        model = Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'summary', 'modified_on')









