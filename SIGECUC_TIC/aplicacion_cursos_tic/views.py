from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from forms import LoginForm

from django.http import HttpResponse

# Create your views here.

def login(request):
	return render_to_response('login.html')

def index(request):
	return render_to_response('index.html')



