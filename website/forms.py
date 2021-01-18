from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, UserProfile, Solving


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password1"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('nickname','bio',)

class SolvingForm(forms.ModelForm):
    class Meta:
        model = Solving
        fields = ('answer','challenge')