from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render , redirect
import datetime as dt
# Create your views here.

def main(request):
    return render(request, 'main.html')

