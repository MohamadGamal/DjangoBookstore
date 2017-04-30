from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as defmodUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,default='a Great author')
    image = models.ImageField(upload_to = 'books/')
    def __str__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,default='a nice book to read')
    pages = models.IntegerField()
    image = models.ImageField(upload_to = 'books/')
    created_at = models.DateTimeField(auto_now_add=True)
    publication = models.DateField()
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)

class User(models.Model):
    # username = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to = 'pics/',null=True)
    # email =models.EmailField(unique=True)
    # password=models.CharField(max_length=200)
    user = models.OneToOneField(defmodUser, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True)
    bio = models.TextField(max_length=500, blank=True)
    likes = models.ManyToManyField(Book,related_name='users_likes')
    read = models.ManyToManyField(Book,related_name='users_read')
    rated = models.ManyToManyField(Book,through='Rate',related_name='users_rated')
    wishes=models.ManyToManyField(Book,related_name='users_wishes')
    follows=models.ManyToManyField(Author)
    favourites=models.ManyToManyField(Category)
    REQUIRED_FIELDS = ('email','password')
class Rate(models.Model):
    rate = models.IntegerField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
# @receiver(post_save, sender=defmodUser)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         User.objects.create(user=instance)

# @receiver(post_save, sender=defmodUser)
# def save_user_profile(sender, instance, **kwargs):
#     instance.user.save()

    
