from django.views.generic import TemplateView,View, DetailView
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import datetime

#Models de la aplicacion cursos
from apps.cursos.models import Curso

#Modelos de aplicacion inicio
from .forms import LoginForm
from apps.cursos.models import MasterTeacher
from apps.cursos.models import LeaderTeacher

#Importamos 
from logica.PerfilFabrica import FabricaPaginaPrincipalUsuario

def pagina_principal(request):
	#funcion que lista los cursos activos cuando el estado es 1
	cursos = Curso.objects.filter(estado='1')
	user = request.user
	context = {'user':user,'cursos':cursos}
	return render_to_response('inicio.html',context)

def pagina_iniciar_sesion(request):
	message = ""

	if request.method == "POST":
		form = LoginForm(request.POST)
		fabriba_pagina_usuario = FabricaPaginaPrincipalUsuario(request)
		pagina_usuario_html = fabriba_pagina_usuario.obtener_pagina_html_usuario(form)
		return pagina_usuario_html.obtener_pagina()

	return render_to_response('login.html',{'message':message}, context_instance=RequestContext(request))

def pagina_perfil(request):
	fabriba_pagina_usuario = FabricaPaginaPrincipalUsuario(request)
	perfil_usuario_html = fabriba_pagina_usuario.obtener_perfil_usuario_html()
	return perfil_usuario_html.obtener_pagina()

def pagina_informacion(request):
	user = request.user
	return render_to_response('informacion.html',{'user':user})


