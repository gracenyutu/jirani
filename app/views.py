from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth import login, authenticate
from .models import Post, Profile, Business, Neighborhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'jirani/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

login_required(login_url='Login')
def profile(request, username):
    return render(request, 'jirani/profile.html')

@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'jirani/edit.html', context)

@login_required(login_url='login')
def upload(request):
    profile = Profile.objects.get(user=request.user)
    profileimage = profile.profile_pic.url
    if request.method == 'POST':
        post = request.FILES['post']
        print(post)
        profile = Profile.objects.get(user=request.user)
        posts = Post.objects.create(user=request.user,photo=post)
        if posts:
            messages.success(request,"post uploaded successfully!")
        else:
            messages.success(request,"post failed!")
    return render(request,'awwards/uploadpost.html',{'profileimage':profileimage})