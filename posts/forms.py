#encoding=UTF-8
from posts.models import Post

__author__ = 'Chus'

from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('owner',)