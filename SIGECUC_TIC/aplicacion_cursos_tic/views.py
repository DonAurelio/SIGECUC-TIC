from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from aplicacion_cursos_tic.forms import LoginForm

# Create your views here.

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

def index_page_view(request):
	return render_to_response('index.html')

def contactenos_page_view(request):
	return render_to_response('contactenos.html')

def quienes_somos_page_view(request):
	return render_to_response('quienes_somos.html')



