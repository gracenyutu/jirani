from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate
from .models import Post, Profile, Business, Neighborhood

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
    return render(request, 'registration/register.html', {'form': form})