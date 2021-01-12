from django.shortcuts import render, redirect  
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Post, Challenge_ZN, Challenge_SC, Challenge_PR
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
        zn_count = Challenge_ZN.objects.all().count()
        zn_id = int((week / zn_count - math.floor(week / zn_count))*zn_count+1)
        sc_count = Challenge_SC.objects.all().count()
        sc_id = int((week / sc_count - math.floor(week / sc_count))*sc_count+1)
        pr_count = Challenge_PR.objects.all().count()
        pr_id = int((week / pr_count - math.floor(week / pr_count))*pr_count+1)
        znalosti= Challenge_ZN.objects.filter(id=zn_id)
        schopnosti= Challenge_SC.objects.filter(id=sc_id)
        pratelstvi= Challenge_PR.objects.filter(id=pr_id)
        context = {
            'znalosti_list': znalosti,
            'schopnosti_list': schopnosti,
            'pratelstvi_list': pratelstvi,
        }
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