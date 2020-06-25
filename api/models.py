from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STATUS_CHOICESS = (
        ('user', 'user'),
        ("moderator", 'moderator'),
        ('admin', 'admin')
    )
    bio = models.TextField(max_length=500, blank=True)
    role = models.CharField(max_length=15, choices=STATUS_CHOICESS, default='user')
    username = models.SlugField(unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)

#class User(AbstractUser):
    #USER_ROLES = (
    #    ('user', 'user'),
    #    ('moderator', 'moderator'),
    #    ('admin', 'admin'),
    #)
    #email = models.EmailField(unique=True)
    #confirmation_code = models.CharField(max_length=16, blank=True, null=True)
    #first_name = models.CharField(max_length=200, blank=True)
    #last_name = models.CharField(max_length=200, blank=True)
    #bio = models.TextField(blank=True, null=True)
    ###role = models.CharField(max_length=10, choices=USER_ROLES, default='user')
    #username = models.SlugField(unique=True, blank=True, null=True)
    #objects = UserManager()
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    rating = models.IntegerField()
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name