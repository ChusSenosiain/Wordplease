#encoding:UTF-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from posts.forms import PostForm
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

    def get(self, request, username, pk):

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

    def get(self, request, username):

        try:
            user = User.objects.filter(username=username)
            posts = Post.objects.filter(owner=user)
            context = {
                'user': user,
                'postlist': posts,
            }

            return render(request, 'blogs/blog_detail.html', context)

        except User.DoesNotExist:
            return HttpResponseNotFound('No existe el blog')



class CreatePostView(View):

    def get(self, request):

        form = PostForm()
        context = {
            'form': form
        }

        return render(request, 'posts/new_post.html', context)

    def post(self, request):

        messages = ''

        post_with_user = Post(owner=request.user)
        form = PostForm(request.POST, instance=post_with_user)
        if form.is_valid():
            new_post = form.save()
            messages = 'Post guardado! <a href="{0}">Ver post</a>'.format(reverse('post_detail', args=[request.user.username, new_post.pk]))
            form = PostForm()

        context = {
            'form': form,
            'message': messages
        }

        return render(request, 'posts/new_post.html', context)


