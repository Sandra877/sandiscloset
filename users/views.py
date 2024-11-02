
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm, LoginForm
from django.http import HttpResponse


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a success page (home page or dashboard)
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def home_view(request):
    return HttpResponse('<h1>Home</h1>')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
