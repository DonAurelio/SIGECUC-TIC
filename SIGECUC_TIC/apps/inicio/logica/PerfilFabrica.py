from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist

from apps.cursos.models import MasterTeacher
from apps.cursos.models import LeaderTeacher

class PerfilHtml:

	def __init__(self,request):
		self.request = request
		self.user = request.user

	def obtener_pagina(self):
		pass

class AdministradorHtml(PerfilHtml):

	def __init__(self,request):
		PerfilHtml.__init__(self,request)

	def obtener_pagina(self):
		return HttpResponseRedirect('admin')

class MasterTeacherHtml(PerfilHtml):

	def __init__(self,request):
		PerfilHtml.__init__(self,request)

	def obtener_pagina(self):
		return render_to_response('master_teacher.html',{'user':self.user})

class LeaderTeacherHtml(PerfilHtml):

	def __init__(self,request):
		PerfilHtml.__init__(self,request)

	def obtener_pagina(self):
		return render_to_response('leader_teacher.html',{'user':self.user})

class ErrorHtml(PerfilHtml):
	def __init__(self,request,message):
		PerfilHtml.__init__(self,request)
		self.message = message

	def obtener_pagina(self):
		return render_to_response('login.html',{'message':self.message},context_instance=RequestContext(self.request))


#Fabrica de paginas de usuario
#Determina y crea la pagina o respuesta http dependiendo 
#del usuario que esta logeado
class FabricaPaginaPrincipalUsuario:

	def __init__(self,request):
		self.request = request
			
		
	def obtener_pagina_html_usuario(self,formulario):
		message = ""
		if formulario.is_valid():
			username = self.request.POST['username']
			password = self.request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(self.request,user)

					#Si el usuario tiene permisos de Administrador 
					#Entonces se redirecciona a la url admin
					if user.is_staff:
						pagina_administrador = AdministradorHtml(self.request)
						return pagina_administrador

					#Si el usuario es Master Teacher o Leader Teacher
					tipo_MasterTeacher = 0 
					tipo_LeaderTeacher = 0
					user_id = user.id

					#Se verifica que tipo de usuario es 
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
						pagina_master_teacher = MasterTeacherHtml(self.request)				
						return pagina_master_teacher
					
					elif tipo_LeaderTeacher == 1:
						pagina_leader_teacher = LeaderTeacherHtml(self.request)
						return pagina_leader_teacher
				
				elif tipo_MasterTeacher == 0 and tipo_LeaderTeacher == 0: 
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
		else:
			message = "Formulario no valido" 
	
		
		error_html = ErrorHtml(self.request,message)
		return error_html

	def obtener_perfil_usuario_html(self):

		#Si el usuario tiene permisos de Administrador 
		#Entonces se redirecciona a la url admin
		user = self.request.user
		if user.is_staff:
			pagina_administrador = AdministradorHtml(self.request)
			return pagina_administrador

		#Si el usuario es Master Teacher o Leader Teacher
		tipo_MasterTeacher = 0 
		tipo_LeaderTeacher = 0
		user_id = user.id

		#Se verifica que tipo de usuario es 
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
			pagina_master_teacher = MasterTeacherHtml(self.request)				
			return pagina_master_teacher
		
		elif tipo_LeaderTeacher == 1:
			pagina_leader_teacher = LeaderTeacherHtml(self.request)
			return pagina_leader_teacher

		