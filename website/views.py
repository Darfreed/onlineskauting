from django.shortcuts import render, redirect  
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Challenge, Category
from django.utils import timezone
import datetime, math

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
        time = datetime.datetime.now()
        week = int(time.strftime("%V"))
        category_count = int(Category.objects.all().count())
        vyzvy = Challenge.objects.filter(id=1)
        print(vyzvy)
        context={
            'vyzvy':vyzvy
        }
        print(context)
        return render(request, self.template_name, context)

class ForumView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/forum.html" 
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(vyzva=False)
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