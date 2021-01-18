from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name="post")
    post = models.TextField(help_text='Napiš něco...')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post
    
    class Meta:
        ordering = ['-date']

class UserProfile(models.Model):
    nickname = models.CharField(max_length=50, blank=True, null=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True,default="Tady můžeš napsat něco o sobě...")

    def __str__(self):
        return self.nickname

class Solving(models.Model):
    solved_by = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name="solved_by")
    challenge = models.ForeignKey("Challenge", on_delete=models.CASCADE, related_name="challenge")
    date = models.DateTimeField(default=timezone.now)
    is_solved = models.BooleanField(default=False)
    answer = models.TextField(blank=True, null=True)
    
    def __str__(self):
        if self.is_solved:
            solved = "Vyhodnoceno"
        else:
            solved = "Nevyhodnoceno"
        return solved+' - '+self.solved_by.nickname+' - '+self.challenge.name

    class Meta:
        ordering = ['is_solved','-date']

class Challenge(models.Model):
    author = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name="author", default=1)
    name = models.CharField(max_length=60,unique=True)
    text = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=60,help_text="blue/red/green")
    
    def __str__(self):
        return self.name