#encoding=UTF-8
__author__ = 'Chus'

from django.contrib.auth.forms import UserCreationForm
from posts.models import Post
from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('owner',)