from django.shortcuts import render, redirect  
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Challenge
from django.utils import timezone

def index(request: HttpRequest) -> HttpResponse:
    return render(request, '../website/index.html', {})

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

class ChallengesView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/challenges.html"
    def get(self, request, *args, **kwargs):
        znalosti= Challenge.objects.filter(kategorie=1)
        schopnosti= Challenge.objects.filter(kategorie=2)
        pratelstvi= Challenge.objects.filter(kategorie=3)
        context = {
            'znalosti_list': znalosti,
            'schopnosti_list': schopnosti,
            'pratelstvi_list': pratelstvi,
        }
        return render(request, self.template_name, context)

class ForumView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/forum.html" 
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'post_list': posts,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        #vyzva = request.POST.get('vyzva')
        autor = request.POST.get("autor")
        #new_post = Post()
        Post().text = text
        #Post().vyzva = vyzva
        Post().autor_id = autor
        Post().datum = timezone.now
        Post().save()
        return redirect(self.template_name)