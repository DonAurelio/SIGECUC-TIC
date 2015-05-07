from django.views.generic import TemplateView,View
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import datetime


from apps.cursos.models import Curso
from .forms import LoginForm
from .models import MasterTeacher
from .models import LeaderTeacher



def pagina_principal(request):
	#funcion que lista los cursos activos cuando el estado es 1
	cursos = Curso.objects.filter(estado='1')
	user = request.user
	context = { 'cursos':cursos,'user':user}
	return render_to_response('inicio.html',context)

def pagina_iniciar_sesion(request):
	message = ""
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					tipo_MasterTeacher = 0 
					tipo_LeaderTeacher = 0
					user_id = user.id
					try:
						master_teacher = MasterTeacher.objects.get(user_id=user_id) #Busca solo un objeto
						tipo_MasterTeacher = 1 #tipo de usuario Mater Teacher
					except ObjectDoesNotExist:
						tipo_MasterTeacher = 0
					try:
						leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
						tipo_LeaderTeacher = 1 #tipo de usuario Mater Teacher
					except ObjectDoesNotExist:
						tipo_LeaderTeacher = 0
						
					if tipo_MasterTeacher == 1:
						form = LoginForm()
						#message = "Te has identificacdo como MasterTeacher " + str(master_teacher.persona.identificacion)
						return render_to_response('master_teacher.html',{'user':user})
					elif tipo_LeaderTeacher == 1:
						return render_to_response('leader_teacher.html',{'user':user})
				elif tipo_MasterTeacher == 0 and tipo_LeaderTeacher == 0: 
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
		else:
			message = "Formulario no valido" 
	else:
		form = LoginForm()

	#return render_to_response('login.html',{'message':message})
	return render_to_response('login.html',{'message':message,'form':form}, context_instance=RequestContext(request))

def pagina_perfil(request):
	user = request.user
	tipo_MasterTeacher = 0 
	tipo_LeaderTeacher = 0
	user_id = user.id
	try:
		master_teacher = MasterTeacher.objects.get(user_id=user_id) #Busca solo un objeto
		tipo_MasterTeacher = 1 #tipo de usuario Mater Teacher
	except ObjectDoesNotExist:
		tipo_MasterTeacher = 0
	try:
		leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
		tipo_LeaderTeacher = 1 #tipo de usuario Mater Teacher
	except ObjectDoesNotExist:
		tipo_LeaderTeacher = 0
		
	if tipo_MasterTeacher == 1:
		form = LoginForm()
		#message = "Te has identificacdo como MasterTeacher " + str(master_teacher.persona.identificacion)
		return render_to_response('master_teacher.html',{'user':user})
	elif tipo_LeaderTeacher == 1:
		return render_to_response('leader_teacher.html',{'user':user})




def pagina_informacion(request):
	user = request.user
	return render_to_response('informacion.html',{'user':user})


