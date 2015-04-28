from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from forms import LoginForm


from django.http import HttpResponse

# Create your views here.

def index_page_view(request):
	return render_to_response('index.html')

def login_page_view(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					
					message = "Te has identificacdo de modo correcto"
				else: 
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = LoginForm()

	return render_to_response('login.html',{'message':message,'form':form}, context_instance=RequestContext(request))
	

def contact_page_view(request):
	return render_to_response('contact.html')

def information_page_view(request):
	return render_to_response('information.html')