from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from enum import Enum

class Category(models.Model):  
    ZNALOSTI = 'ZN'
    SCHOPNOSTI = 'SC'
    PRATELSTVI = 'PR'
    CATEGORY_CHOICES = (
        (ZNALOSTI, 'Znalosti'),
        (SCHOPNOSTI, 'Schopnosti'),
        (PRATELSTVI, 'Přátelství'),
    )
    category = models.CharField(max_length=2,choices=CATEGORY_CHOICES, default=ZNALOSTI, unique=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    autor = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name="post")
    text = models.TextField()
    vyzva = models.BooleanField("vyzva")
    datum = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-datum']

class UserProfile(models.Model):
    nickname = models.CharField(max_length=50, blank=True, null=True, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nickname

class Challenge(models.Model):
    splněno = models.ManyToManyField(UserProfile,blank=True, null=True)
    nazev = models.CharField(max_length=60)
    text = models.TextField()
    kategorie =  models.ForeignKey("Category", on_delete=models.CASCADE,)

    def __str__(self):
        return self.nazev
