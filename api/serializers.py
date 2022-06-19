from rest_framework import serializers
from app.models import Business, Profile, Post, Neighborhood
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic', 'bio', 'contact']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'description', 'technologies', 'photo', 'date', 'user']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    posts = PostSerializer(many=True, read_only=True)

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ['hoodname', 'location', 'hoodphoto', 'description', 'healthdep', 'policeno']

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['name', 'email', 'description']