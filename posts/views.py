#encoding:UTF-8
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