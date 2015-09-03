#encoding:UTF-8

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, FormView
from posts.forms import PostForm, loginForm, SignUpForm
from posts.models import Post
from wordplease.settings import PUBLIC


# Home Page: shows the last 5 post ordered by update date
class HomeView(View):

    def get(self, request):

        # Get the public posts, desc order
        posts = Post.objects.filter(visibility=PUBLIC).order_by('-modified_on')
        context = {
            'postlist':posts[:5],
        }

        return render(request, 'posts/home.html', context)


# Post detail View
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


# Blog list View: a list with all the blogs
class BlogsView(View):

    def get(self, request):

        blogs = User.objects.all()

        context = {
            'bloglist':blogs,
        }

        return render(request, 'blogs/blog_list.html', context)



# Blog detail: shows a list of blog's posts.
class BlogView(View):

    def get(self, request, username):

        try:
            user = User.objects.filter(username=username)
            posts = Post.objects.filter(owner=user).order_by('-modified_on')
            context = {
                'user': user,
                'postlist': posts,
            }

            return render(request, 'blogs/blog_detail.html', context)

        except User.DoesNotExist:
            return HttpResponseNotFound('No existe el blog')


# User profile view: shows the user blog
class ProfileView(View):

    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        context = {
            'username': request.user.username
        }
        return redirect('blog_detail', username=request.user.username)


# Login view
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


# Sign Up, create an user
class SignupView(FormView):

    template_name = 'users/signup.html'
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username', '')
        password = form.cleaned_data.get('password1', '')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('home')


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            logout(request)
        return redirect(reverse('home'))


# Create a post: only logged users can create a post
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

