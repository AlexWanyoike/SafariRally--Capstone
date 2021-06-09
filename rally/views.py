from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render , redirect
import datetime as dt
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MoringaMerch
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly
# Create your views here.

def main(request):
    return render(request, 'main.html')

