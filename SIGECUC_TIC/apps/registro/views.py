from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.contrib.auth.models import User
from apps.cursos.models import MasterTeacher
from .forms import UserForm
from .forms import PersonaForm


def pagina_registro(request):
	return render_to_response('registro.html')

def pagina_registrar_master_teacher(request):

	if request.method == "POST":
		form_user = UserForm(request.POST)
		form_persona = PersonaForm(request.POST)

		if form_user.is_valid() and form_persona.is_valid():
			add_user = form_user.save(commit=False)#noguarda todavia los datos semantienen
			username = request.POST.get('username')
			password = request.POST.get('password')	
			user = User.objects.create_user(username=username, password=password)
			user.save()

			add_persona = form_persona.save(commit=False)#noguarda todavia los datos semantienen
			ide_persona = form_persona.instance.pk #trae el id deacuerdo al form
			add_persona.save()#Guardamos la informacion

			ide_user= User.objects.get(username=username)
			master_teacher= MasterTeacher(ide_user.id, ide_persona)
			master_teacher.save()
			mensaje = "Su inscripcion se ha realizado con exito" 
			user = request.user
			contexto = {'user':user, 'mensaje':mensaje}
			return render_to_response('registrar_master_teacher.html', contexto)
		else:
			form_persona = PersonaForm(request.POST)	
	else:
		form_user = UserForm()
		form_persona = PersonaForm()
	user = request.user
	ctx = {'user':user ,'form_persona':form_persona, 'form_user': form_user}
	return render_to_response('registrar_master_teacher.html', ctx, context_instance= RequestContext(request))

