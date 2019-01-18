from django.shortcuts import render

# this is required for the responses
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Hello World</h1>')
