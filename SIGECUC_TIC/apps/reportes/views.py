from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from apps.cursos.models import LeaderTeacher
from logica.estudiante import Estudiante

# Create your views here.

#@login_required(login_url='login/')	
def principal(request):
	user = request.user
	mensaje = " bienvenid@ al modulo de reportes,"
	mensaje += " por favor seleccione el reporte que "
	mensaje += "desea visualzar."
		
	contexto = {'user':user, 'mensaje':mensaje}
	return render_to_response('principal.html',contexto)


#@login_required(login_url='login/')	
def reporte_notas_por_estudiantes(request):
	user = request.user
	estudiantes = LeaderTeacher.objects.all()
	estudiantes_calificados = []
	for estudiante in estudiantes:
		estudiantes_calificados.append(Estudiante(estudiante))
	
	contexto = {'user':user,'estudiantes':estudiantes_calificados}

	return render_to_response('tabla1.html',contexto)
