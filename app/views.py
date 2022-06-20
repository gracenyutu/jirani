from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, UpdateUserForm, UpdateUserProfileForm, PostForm, JiraniForm
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
    return render(request,'jirani/uploadpost.html',{'profileimage':profileimage})

def search(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        results = Post.objects.filter(title__icontains=title).all()
        print(results)
        message = f'name'
        context = {'results': results,'message': message}
        return render(request, 'jirani/search.html', context)
    else:
        message = "You haven't searched for any site"
    return render(request, 'jirani/search.html', {'message': message})

def newhood(request):
    if request.method == 'POST':
        form = JiraniForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('jirani')
    else:
        form = JiraniForm()
    return render(request, 'jirani/newhood.html', {'form': form})


def joinahood(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('jirani')


def leaveahood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('jirani')

def hoods(request):
    hoods = Neighborhood.objects.all()
    hoods = hoods[::-1]
    context = {
        'hoods': hoods,
    }
    return render(request, 'jirani/jirani.html', context)

def hood(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighborhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == 'POST':
        form = JiraniForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.neighbourhood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('hood', hood.id)
    else:
        form = JiraniForm()
    context = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'jirani/hood.html', context)


def occupants(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    occupants = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'jirani/occupants.html', {'occupants': occupants})
