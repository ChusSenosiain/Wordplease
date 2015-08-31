#encoding:UTF-8
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from posts.models import Post
from wordplease.settings import PUBLIC


class HomeView(View):

    def get(self, request):

        #Get the public posts, desc order
        posts = Post.objects.filter(visibility=PUBLIC).order_by('-created_on')
        context = {
            'postlist':posts[:5],
        }

        return render(request, 'posts/home.html', context)




class PostView(View):

    def get(self, request, pk):

        try:
            post = Post.objects.get(pk=pk)

            context = {
                'post':post,
            }

            return render(request, 'posts/post_detail.html', context)

        except Post.DoesNotExist:
            return HttpResponseNotFound('No existe el post')



class BlogsView(View):

    def get(self, request):

        blogs = User.objects.all()

        context = {
            'bloglist':blogs,
        }

        return render(request, 'blogs/blog_list.html', context)


class BlogView(View):

    def get(self, request, pk):

        try:
            user = User.objects.get(pk=pk)
            context = {
                'user':user,
            }

            return render(request, 'blogs/blog_detail.html', context)

        except User.DoesNotExist:
            return HttpResponseNotFound('No existe el blog')

