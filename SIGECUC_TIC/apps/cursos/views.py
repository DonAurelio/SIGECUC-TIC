from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse

from forms import InscripcionPersonaForm
from forms import HistorialLaboralForm
from forms import HistorialAcademicoForm
from .models import Curso
from .models import Inscrito
import datetime



# Create your views here.

#======================================> MASTER TEACHER VIEWS <===========================================
def pagina_master_teacher_informacion_personal(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('master_teacher_estudiantes.html',contexto)

def pagina_master_teacher_actividades_evaluacion(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('master_teacher_actvidades_de_evaluacion.html',contexto)

def pagina_master_teacher_estudiantes(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('master_teacher_estudiantes.html',contexto)

#======================================> LEADER TEACHER VIEWS <===========================================

def pagina_leader_teacher_informacion_personal(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('leader_teacher_informacion_personal.html',contexto)

def pagina_leader_teacher_informacion_curso(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('leader_teacher_informacion_curso.html',contexto)

def pagina_leader_teacher_calificaciones(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('leader_teacher_calificaciones.html',contexto)

def pagina_leader_teacher_historial_academico(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('leader_teacher_historial_academico.html',contexto)

def pagina_leader_teacher_certificados_obtenidos(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('leader_teacher.html',contexto)







