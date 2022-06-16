from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    hoodname = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    occupants = models.IntegerField(null=True, blank=True)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    healthdep = models.IntegerField(null=True, blank=True)
    policeno = models.IntegerField(null=True, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='media/images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    contact = models.EmailField(max_length=100, blank=True)
    location = models.CharField(max_length=60, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

class Business(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='business_owner', blank=True)
    name = models.CharField(blank=True, max_length=120)
    description = models.TextField(blank=True)

class Post(models.Model):
    title = models.CharField(max_length=155)
    post = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='media/posts/', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="post")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='post_owner', blank=True)
