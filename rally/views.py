from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render , redirect
import datetime as dt
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core import exceptions
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from .models import * 
from .serializer import *
from rest_framework import status
from django.http import JsonResponse
#from .permissions import IsAdminOrReadOnly
# Create your views here.

def main(request):
    post = request.GET.get('post')
    post = Post.objects.all()
    context = {'post': post }
    return render(request, 'main.html' , context)

def profile(request , username):
    date = dt.date.today()
    # post = Post.objects.get(pk=pk)
    # profile = Profile.objects.get(pk=pk)
    post = Post.get_post_by_user(username)
    profile = Profile.get_profile(username)
    context = {'post': post,'profile': profile, 'date': date}
    return render(request ,'profile.html' , context)

    # def user_profile(request, username):
    
    # date = dt.date.today()
    # images = Image.get_image_by_user(username)
    # profile = Profile.get_profile(username)

    # context = {'images': images ,'profile': profile, 'date': date}

    # return render(request ,'profile.html' , context )
    

def details(request , pk):
    post = Post.objects.all()
    post = Post.objects.get(id=pk)
    profile = Profile.objects.all()
    comments = Comment.objects.all()
    context = {'post': post , 'profile': profile , 'comments': comments}
    return render(request ,'details.html', context)

def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
                
        return redirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'create_profile.html', {"form": form})
    

def edit_profile(request):
    return render(request, 'edit_profile.html')

def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return HttpResponseRedirect('/')
           
    else:
        form = CreatePostForm()
        return render(request, 'create_post.html', {"form": form})


def login(request):
    return render(request , 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('main')
    else:
        form = UserRegisterForm()
    return render(request ,'/accounts/login.html' , {'form': form})

def comment(request):
    return render(request , 'comment.html')


