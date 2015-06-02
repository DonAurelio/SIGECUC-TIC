from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import ObjectDoesNotExist

from apps.inscripcion.forms import *

from apps.cursos.models import Inscrito
from apps.cursos.models import Cursos_Inscrito

from logica.utilidad import TraductorFecha
from logica.utilidad import EmailSender

import datetime


class AbstractBuilder:

	def build_part(self,request):
		pass

	def get_result(self):
		pass


class InscriptionBuilder(AbstractBuilder):

	#Definimos la variable que tendra el resultado de alguna de las operaciones
	#Implementadas
	def __init__(self):
		self.result = None

	#Construye la inscripcion
	def build_part(self,request):
		if request.method == "POST":
			if self.inscription_form_valid(request):
				self.build_inscription(request)
			else:
				self.build_inscription_form_invalid(request)
		else:
			self.build_inscription_form(request)

	#Retorna el resultado de crear una incripcion 
	def get_result(self):
		return self.result

	#Construimos (crear en la base de datos) la inscripcion del usuario
	def build_inscription(self,request):
		info = "iniciado"
		id_course = request.GET.get('id_course')
		name_course = request.GET.get('name_course')

		form_persona = InscripcionPersonaForm(request.POST)
		form_HistorialAcademico = HistorialAcademicoForm(request.POST) 
		form_HistorialLaboral = HistorialLaboralForm(request.POST)

		add_persona = form_persona.save(commit=False)#noguarda todavia los datos semantienen
		add_HistorialAcademico = form_HistorialAcademico.save(commit=False)#n oguarda todavia los datos semantienen
		add_HistorialLaboral = form_HistorialLaboral.save(commit=False)#n oguarda todavia los datos semantienen
		add_persona.save()#Guardamos la informacion
		ide_persona = form_persona.instance.pk #trae el id deacuerdo al form
		add_HistorialAcademico.save()
		ide_historialAcademico = form_HistorialAcademico.instance.pk
		add_HistorialLaboral.save() 
		ide_historialLaboral = form_HistorialLaboral.instance.pk
		form_persona.save_m2m() #Guarda las relaciones de ManyToMany
		form_HistorialAcademico.save_m2m() #Guarda las relaciones de ManyToMany
		form_HistorialLaboral.save_m2m() #Guarda las relaciones de ManyToMany
		
		fecha_actual =  datetime.datetime.now()
		numero_mes = datetime.datetime.now().month
		fecha_transformada = TraductorFecha(datetime.datetime.now())
		mes = fecha_transformada.get_mes()
		dia = fecha_transformada.get_dia()
		anio = fecha_transformada.get_anio()

		inscrip= Inscrito(ide_persona, dia, mes, anio, True, ide_historialLaboral,ide_historialAcademico)
		curso_inscrito = Cursos_Inscrito(curso_id=id_course, inscrito_id=ide_persona, fecha_inscripcion=fecha_actual, estado='Pendiente')
		inscrip.save()
		curso_inscrito.save()

		email = request.POST.get('email')
		EmailSender(email, name_course)
		mensaje = "Su inscripcion se ha realizado con exito, se ha enviado una notificacion al correo %s" %email 
		contexto = {'mensaje':mensaje}
		self.result = render_to_response('inscripcion.html',contexto)


	#Verifica si todos los formularios de la inscripcion son validos
	def inscription_form_valid(self,request):
		form_persona = InscripcionPersonaForm(request.POST)
		form_HistorialAcademico = HistorialAcademicoForm(request.POST) 
		form_HistorialLaboral = HistorialLaboralForm(request.POST)
		return form_persona.is_valid() and form_HistorialAcademico.is_valid() and form_HistorialLaboral.is_valid()

	#Constuirmos el formulario para ser diligenciado 
	def build_inscription_form(self,request):

		info = "iniciado"
		id_course = request.GET.get('id_course')
		name_course = request.GET.get('name_course')

		form_persona = InscripcionPersonaForm()
		form_HistorialAcademico = HistorialAcademicoForm() 
		form_HistorialLaboral = HistorialLaboralForm()

		ctx = {
		'form_persona':form_persona, 
		'form_HistorialLaboral': form_HistorialLaboral,
		'form_HistorialAcademico': form_HistorialAcademico,
		 'informacion':info, 'id_course':id_course, 'name_course':name_course}
		self.result = render_to_response('inscripcion.html', ctx, context_instance= RequestContext(request))

	def build_inscription_form_invalid(self,request):
		
		info = "iniciado"
		id_course = request.GET.get('id_course')
		name_course = request.GET.get('name_course')

		form_persona = InscripcionPersonaForm(request.POST)
		form_HistorialAcademico = HistorialAcademicoForm(request.POST) 
		form_HistorialLaboral = HistorialLaboralForm(request.POST)

		ctx = {
		'form_persona':form_persona, 
		'form_HistorialLaboral': form_HistorialLaboral,
		'form_HistorialAcademico': form_HistorialAcademico,
		 'informacion':info, 'id_course':id_course, 'name_course':name_course}
		self.result = render_to_response('inscripcion.html', ctx, context_instance= RequestContext(request))



class InscriptionDirector:
	def __init__(self):
		self.builder = InscriptionBuilder()

	def construct(self,request):
		self.builder.build_part(request)
		return self.builder.get_result()


