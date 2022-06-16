from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    hoodname = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    occupants = models.IntegerField()
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='media/images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    contact = models.EmailField(max_length=100, blank=True)
