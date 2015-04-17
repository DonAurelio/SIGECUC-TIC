from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from forms import LoginForm


# Create your views here.
#Vista para el sistema de login de un usuario
def login_page(request):
	mensaje = None

	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			nombre_usuario = request.POST['nombre_usuario']
			contrasenia = request.POST['contrasenia']
			user = authenticate(username=nombre_usuario,password=contrasenia)
			if user is not None:
				if user.is_active:
					login(reques, user)
					mensaje = "Te has identificado de modo correcto"
				else:
					mensaje = "Tu usuario esta inactivo"

			else:
				mensaje = "Nombre de usuario y/o password incorrectos"

	else:
		form = LoginForm()

	return render_to_response('login.html',{'mensaje':mensaje, 'form':form},
		context_instance=RequestContext(request))