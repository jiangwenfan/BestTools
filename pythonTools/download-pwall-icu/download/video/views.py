from django.shortcuts import render

# Create your views here.

def index(request):
    render('index.html')

def video_get(request):
    request.post
