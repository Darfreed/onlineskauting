from django.shortcuts import render, redirect  
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Challenge, Category, Solving, UserProfile
from django.contrib.auth.models import User
from .forms import RegisterForm, PostForm, UserProfileForm, SolvingForm
import datetime, math

from django import template
register = template.Library()


def index(request: HttpRequest) -> HttpResponse:
    return render(request, '../website/index.html', {})

class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html" 

    def get(self, request, *args, **kwargs):
        username = None
        if request.user.is_authenticated:
            username = request.user.profile
        challenges = Solving.objects.filter(solved_by=username).order_by('challenge__category__name', '-is_solved','challenge__id')
        category_list = Category.objects.all()
        znalosti_img='images/avatar/zn_'+str(Solving.objects.filter(is_solved=True,solved_by=username,challenge__category__name="Znalosti").count())+'.png'
        schopnosti_img='images/avatar/sc_'+str(Solving.objects.filter(is_solved=True,solved_by=username,challenge__category__name="Schopnosti").count())+'.png'
        pratelstvi_img='images/avatar/pr_'+str(Solving.objects.filter(is_solved=True,solved_by=username,challenge__category__name="Přátelství").count())+'.png'
        my_record = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(instance=my_record)
        context = {
            'challenges': challenges,
            'category_list': category_list,
            'pratelstvi_img':pratelstvi_img,
            'schopnosti_img':schopnosti_img,
            'znalosti_img':znalosti_img,
            'form':form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        profil = UserProfile.objects.get(user=request.user)
        form = UserProfileForm(request.POST, instance=profil)
        if form.is_valid():
            profil.save()

            bio = form.cleaned_data['bio']
            return redirect(self.template_name)
        
        args = {'form':form,'bio':bio}
        return render(request, self.template_name, args)

class ChallengesView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/challenges.html"

    def get(self, request, *args, **kwargs):
        
        form = SolvingForm()
        if request.user.is_authenticated:
            username = request.user.profile
        time = datetime.datetime.now()
        week = int(time.strftime("%V"))
        challenge_list = Challenge.objects.none()
        category_list = Category.objects.all()
        solved_list = Solving.objects.filter(is_solved=True,solved_by=username)
        i = 0
        while i < Category.objects.all().count():
            in_category = Challenge.objects.filter(category=category_list[i].id)
            in_category_count = Challenge.objects.filter(category=category_list[i].id).count()
            challenge = int((week / in_category_count - math.floor(week / in_category_count))*in_category_count)
            challenge_id = in_category[challenge].id
            challenge_list |= Challenge.objects.filter(id=challenge_id)
            i = i + 1
        context = {
            'challenge_list':challenge_list,
            'category_list':category_list,
            'solved_list':solved_list,
            'form':form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SolvingForm(request.POST)
        if form.is_valid():

            solving = form.save(commit=False)
            solving.solved_by = request.user.profile
            solving.challenge = Challenge.objects.get(pk=form.cleaned_data['challenge'])
            solving.save()

            return redirect(self.template_name)
        
        args = {'form':form}
        return render(request, self.template_name, args)

class ForumView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/forum.html" 

    def get(self, request, *args, **kwargs):
        form = PostForm()
        posts = Post.objects.all()
        context = {
            'post_list': posts,
            'form':form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()

            text = form.cleaned_data['post']
            form = PostForm()
            return redirect(self.template_name)
        
        args = {'form':form,'text':text}
        return render(request, self.template_name, args)
