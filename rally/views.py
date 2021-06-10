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

