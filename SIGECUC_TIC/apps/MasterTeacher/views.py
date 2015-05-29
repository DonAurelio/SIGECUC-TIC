from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
#from .forms import Persona_MasterTeacherForm
from apps.cursos.forms import Informacion_personalForm
from apps.cursos.models import MasterTeacher
from apps.cursos.models import Cohorte
from apps.cursos.models import Curso
from apps.cursos.models import LeaderTeacher
from apps.cursos.models import Calificacion
from apps.cursos.models import Asistencia
from logica.utilidad import TraductorFecha

from decimal import Decimal
import datetime


# Create your views here.

def pagina_master_teacher_informacion_personal(request):
	user = request.user
	user_id = user.id
	#consulta a Mater Teacher
	master_teacher = MasterTeacher.objects.get(user_id=user_id)
	master_teacher_id = master_teacher.persona.identificacion
	cohortes = Cohorte.objects.filter(master_teacher_id=master_teacher_id)


	if request.method == "POST":
		#se instancia el master_teacher para que pase la validez y sea un formulario para modificar
		form_personaMasterTeacher = Informacion_personalForm(request.POST, instance=master_teacher)
		if form_personaMasterTeacher.is_valid():
			email = form_personaMasterTeacher.cleaned_data["email"]
			master_teacher.persona.email = email
			telefono = form_personaMasterTeacher.cleaned_data["telefono"]
			master_teacher.persona.telefono = telefono
			direccion = form_personaMasterTeacher.cleaned_data["direccion"]
			master_teacher.persona.direccion = direccion
			master_teacher.persona.save()
			mensaje = "Su informacion personal ha sido modificada correctamente"
			return render_to_response('master_teacher.html',{'user':user,'mensaje':mensaje})
	
	else:
		form_personaMasterTeacher = Informacion_personalForm(request.POST, instance= master_teacher) 

		form_personaMasterTeacher = Informacion_personalForm(initial = {'identificacion' : master_teacher.persona.identificacion, 
			'primer_nombre' : master_teacher.persona.primer_nombre, 'segundo_nombre' : master_teacher.persona.segundo_nombre,
			'primer_apellido': master_teacher.persona.primer_apellido, 'segundo_apellido' : master_teacher.persona.segundo_apellido,
			'email' : master_teacher.persona.email, 'telefono' : master_teacher.persona.telefono, 
			'direccion' : master_teacher.persona.direccion

			})
	contexto = {'user':user, 'form_personaMasterTeacher' : form_personaMasterTeacher,'cohortes':cohortes}
	return render_to_response('master_teacher_informacion_personal.html',contexto, context_instance= RequestContext(request))

#=================================>CALIFICANCIONES PARA MASTER TEACHER<=======================================================
def esta_calificacion(request,leader_teacher_id, cohorte_id, actividad_id):
		#Se verifica si la calificacion esta guardada 
		try:
			modificar_calificacion = Calificacion.objects.get(leader_teacher_id=leader_teacher_id,
					cohorte_id=cohorte_id, actividad_id=actividad_id)
			return modificar_calificacion
		except ObjectDoesNotExist:
			return False

def guardar_notas_html(request, estudiantes, curso, id_cohorte):
	#funcion que guarda las notas de los leader_Teacher
	#campo_nota = ""
	for estudiante in estudiantes:
		for actividad in curso.actividad_evaluacion.all():
			campo_nota = request.POST.get(''+estudiante.inscrito.persona.identificacion+'#'+str(actividad.id)+'')
			modificar_calificacion = esta_calificacion(request, estudiante.inscrito.persona.identificacion, id_cohorte,
				actividad.id)
			if modificar_calificacion:
				#ya esta guardada la calificacion entonces se modifica
				modificar_calificacion.nota_actividad = campo_nota
				modificar_calificacion.save()
			else:
				#aqui guarda la primera vez las notas
				calificar = Calificacion(nota_actividad=campo_nota, leader_teacher_id=estudiante.inscrito.persona.identificacion,
				cohorte_id=id_cohorte, actividad_id=actividad.id)
				calificar.save()

def consultar_calificaciones(request, id_cohorte):
		#funcion esta en construccion
		try:
			consulta_calificacion = Calificacion.objects.filter(cohorte__id=id_cohorte).order_by('leader_teacher_id')
			return consulta_calificacion
		except ObjectDoesNotExist:
			return False



def pagina_master_teacher_actividades_evaluacion(request, cohorte_id):
	user = request.user
	user_id = user.id
	
	master_teacher = MasterTeacher.objects.get(user_id=user_id)
	master_teacher_id = master_teacher.persona.identificacion

	cohortes = Cohorte.objects.filter(master_teacher_id=master_teacher_id)
	#id_cohorte = request.GET.get('id_cohorte')
	id_cohorte = cohorte_id
	cohorte = Cohorte.objects.get(id=id_cohorte)
	curso_id=cohorte.curso.id
	#se consulta el curso
	curso = Curso.objects.get(id=curso_id)
	#consulta los Leader Teacher pertenecientes a la cohorte 
	estudiantes = LeaderTeacher.objects.filter(cohorte__id=id_cohorte).order_by('inscrito_id')
	if request.method == 'POST':
		#funcion que guarda en la base de datos los campo de plantillas
		#obtiene el campo dependiendo de su identificacion y su actividad
		guardar_notas_html(request, estudiantes, curso, id_cohorte)
		#campo_nota = request.POST.get('6558889#2')
		#datos_iden_activi = dividir_campo_nota(campo_nota)
		return HttpResponse ("calificado")
	else:
		#Codigo cuando se carga la pagina
		#===================================================================================================
		consulta_calificacion = consultar_calificaciones(request, id_cohorte)
		calificaciones_curso = []
		for estudiante in estudiantes:
			calififcaciones_estudiante = Calificacion.objects.filter(leader_teacher_id=estudiante.inscrito.persona.identificacion,cohorte_id=id_cohorte)
			calificaciones_curso.append(calififcaciones_estudiante)
		estudiantes_calificaciones = zip(estudiantes,calificaciones_curso)

		#===================================================================================================
		actividad_evaluacion = curso.nombre
		if consulta_calificacion:
			#si tiene calificacion validador True para que muestre el foermulario con las notas
			validador = True
		else:
			validador = False
		contexto = {'cohorte': cohorte, 'curso': curso, 'estudiantes': estudiantes,'cohortes':cohortes, 
		'estudiantes_calificaciones':estudiantes_calificaciones, 'validador':validador}
		return render_to_response('master_teacher_actividades_de_evaluacion.html',contexto, context_instance= RequestContext(request))
		#html = "<html><body><h1>id cohorte:</h1><h3>%s<h/3> <h1> Name curso</h1><h2><h/2></body></html>" % curso
		#return HttpResponse(html)

#=================================>FIN CALIFICANCIONES PARA MASTER TEACHER<=====================================================


#=================================>Inicio Asistencia estudiante<=======================================================

def pagina_master_teacher_asistencia_estudiante(request, cohorte_id):
	user = request.user
	user_id = user.id
	
	master_teacher = MasterTeacher.objects.get(user_id=user_id)
	master_teacher_id = master_teacher.persona.identificacion

	cohortes = Cohorte.objects.filter(master_teacher_id=master_teacher_id)
	#id_cohorte = request.GET.get('id_cohorte')
	id_cohorte = cohorte_id
	cohorte = Cohorte.objects.get(id=id_cohorte)
	curso_id=cohorte.curso.id
	#se consulta el curso
	curso = Curso.objects.get(id=curso_id)

	fecha_transformada = TraductorFecha(datetime.datetime.now())
	mes = fecha_transformada.get_mes()
	dia = fecha_transformada.get_dia()
	anio = fecha_transformada.get_anio()
	#verifica cantidad de asistente
	cantidad_asistencia = Asistencia.objects.filter(cohorte__id=id_cohorte, dia=dia, 
		mes=mes, anio=anio).count()
	if(cantidad_asistencia !=0):
		mensaje = "Ya ha sido registrada la asistencia en la fecha de hoy"
		contexto = {'cohorte': cohorte, 'curso': curso,'cohortes':cohortes, 'mensaje': mensaje}
		return render_to_response('master_teacher_asistencia_estudiante.html',contexto, context_instance= RequestContext(request))

	#consulta los Leader Teacher pertenecientes a la cohorte 
	estudiantes = LeaderTeacher.objects.filter(cohorte__id=id_cohorte).order_by('inscrito_id')
	if request.method == 'POST':
		fecha_transformada = TraductorFecha(datetime.datetime.now())
		mes = fecha_transformada.get_mes()
		dia = fecha_transformada.get_dia()
		anio = fecha_transformada.get_anio()
		cantidad_registro = 0 #valida cuantos registros han sido guardados
		for estudiante in estudiantes:
			asistencia = request.POST.get(''+estudiante.inscrito.persona.identificacion)
			if(not asistencia is None):
				cantidad_registro += 1
				guardar_asistencia = Asistencia(leader_teacher_id = estudiante.inscrito.persona.identificacion,
					cohorte_id=id_cohorte, dia=dia, mes=mes, anio=anio)	
				guardar_asistencia.save()
		#compara si ha sido registrado un asistente
		if cantidad_registro == 0:
			mensaje = "No se ha registrado la asistencia por favor seleccione los asistentes"	
		else:
			mensaje = "Se ha registrado la asistencia"					
		contexto = {'cohorte': cohorte, 'curso': curso, 'estudiantes': estudiantes,'cohortes':cohortes, 
		'mensaje':mensaje}
		return render_to_response('master_teacher_asistencia_estudiante.html',contexto, context_instance= RequestContext(request))

	else:
		contexto = {'cohorte': cohorte, 'curso': curso, 'estudiantes': estudiantes,'cohortes':cohortes}
		return render_to_response('master_teacher_asistencia_estudiante.html',contexto, context_instance= RequestContext(request))

#=================================>FIN Asistencia estudiante<=======================================================
