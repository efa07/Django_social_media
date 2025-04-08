from django.shortcuts import render
from django.http import HttpResponse as HR

def index(req):
    return render(req, 'index.html')