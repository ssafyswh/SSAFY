from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User


# Create your views here.

def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('todos:index')
  else:
    form = CustomUserCreationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/signup.html', context)

def login(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      auth_login(request, form.get_user())
      return redirect('todos:index')
  else:
    form = AuthenticationForm()
  context = {
    'form': form
  }
  return render(request, 'accounts/login.html', context)

def logout(request):
  auth_logout(request)
  return redirect('todos:index')

def profile(request, username):
  user = User.objects.get(username=username)
  context = {
    'user': user
  }
  return render(request, 'accounts/profile.html', context)

# 로그인하지 않은 유저가 팔로우 기능 사용시 로그인 페이지로 이동
@login_required
def follow(request, user_pk):
  user = User.objects.get(pk=user_pk)
  if request.user != user: 
    if request.user in user.followers.all(): 
      request.user.followings.remove(request.user) 
    else: 
      request.user.followings.add(request.user) 
  return redirect('accounts:profile', user.username)


def following(request, user_pk):
  user = User.objects.get(pk=user_pk)
  context = {
    'user': user
  }
  return render(request, 'accounts/following.html', context)

def followers(request, user_pk):
  user = User.objects.get(pk=user_pk)
  context = {
    'user': user
  }
  return render(request, 'accounts/followers.html', context)