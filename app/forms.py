from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Business, Neighborhood

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_pic', 'bio', 'location']

class PostForm(forms.ModelForm):
    photo = forms.ImageField(label='')

    class Meta:
        model = Post
        fields = ('photo', 'title', 'post' )

class JiraniForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ('admin',)