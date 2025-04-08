from django.shortcuts import render
from django.http import HttpResponse as HR

def index(req):
    return HR("<h1>Welcome Home</h1>")