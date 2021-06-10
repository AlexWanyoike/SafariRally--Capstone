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
    return render(request, 'main.html')

def profile(request):
    return render(request, 'profiile.html')

def detail(request):
    return render(request , 'details.html')

def create_profile(request):
    return render(request, 'create_profile.html')

def edit_profile(request):
    return render(request, 'edit_profile.html')

def create_post(request):
    return render(request , 'create_post.html')

def login(request):
    return render(request , 'login.html')

def register(request):
    return render(request , 'register.html')


