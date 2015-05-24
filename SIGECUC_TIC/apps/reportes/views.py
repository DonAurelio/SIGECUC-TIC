from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from apps.cursos.models import LeaderTeacher, Curso
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


def reporte_estudiantes_cursos_aprobados(request):
	user = request.user
	leader_teachers = LeaderTeacher.objects.all()
	estudiantes_curso_aprobado = []
	for leader_teacher in leader_teachers:
		estudiante = Estudiante(leader_teacher)
		if estudiante.aprobo_almenos_un_curso:
			estudiantes_curso_aprobado.append(estudiante)
	
	contexto = {'user':user,'estudiantes':estudiantes_curso_aprobado}

	return render_to_response('tabla2.html',contexto)

def reporte_estudiantes_curso_por_departamento(request):
	user = request.user
	cursos = Curso.objects.all()
	if request.method == "POST":
		pass

	contexto = {'user':user, 'cursos': cursos}
	return render_to_response('tabla3_consulta.html',contexto)
	


