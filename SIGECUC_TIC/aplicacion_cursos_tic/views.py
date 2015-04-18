from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from forms import LoginForm


# Create your views here.

class home(TemplateView):
	pass

class Login(TemplateView):
	template_name = 'login.html'
	form_login = LoginForm()

	def get(self,request,*args,**kwargs):
		return render(request,self.template_name,{'form':self.form_login})

	def post(self,request,*args,**kwargs):
		mensaje = ""
		self.form_login = LoginForm(request.POST)
		if self.form_login.is_valid():
			nombre_usuario = request.POST['nombre_usuario']
			contrasenia = request.POST['contrasenia']
			user = authenticate(username=nombre_usuario,password=contrasenia)
			if user is not None:
				if user.is_active:
					login(request, user)
					mensaje = "Te has identificado de modo correcto"
				else:
					mensaje = "Tu usuario esta inactivo"

			else:
				mensaje = "Nombre de usuario y/o password incorrectos"
		return render(request,self.template_name,{'mensaje':mensaje,'form':self.form_login})

