from django.shortcuts import render_to_response

#Modulos django
from django.template import RequestContext

#Models de la aplicacion cursos
from apps.cursos.models import Curso, MasterTeacher, LeaderTeacher

#Formulario de la aplicacion inicio
from .forms import LoginForm

#Se importa el patron de disenio fabrica de perfiles 
from logica.perfil_fabrica import FabricaPaginaPrincipalUsuario

def pagina_principal(request):
	#Listamos los cursos que tiene como estado 1 (activo)
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


