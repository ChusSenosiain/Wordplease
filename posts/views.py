#encoding:UTF-8
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from posts.forms import PostForm, loginForm
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



class ProfileView(View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        context = {
            'username': request.user.username
        }
        return redirect('blog_detail', username=request.user.username)


class LoginView(View):

    def get(self, request):

        form = loginForm(request.POST or None)
        context = {
            'form': form
        }

        return render(request, 'users/login.html', context)

    def post(self, request):

        form = loginForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            user_username = form.cleaned_data.get('username','')
            user_password =  form.cleaned_data.get('password', '')
            user = authenticate(username=user_username, password=user_password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    context['errors'] = 'El usuario no está activo'
            else:
                context['errors'] = 'Usuario o contraseña incorrectos'


        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            logout(request)
        return redirect(reverse('home'))


class CreatePostView(View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request):

        form = PostForm()
        context = {
            'form': form
        }

        return render(request, 'posts/new_post.html', context)

    @method_decorator(login_required(login_url='login'))
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

