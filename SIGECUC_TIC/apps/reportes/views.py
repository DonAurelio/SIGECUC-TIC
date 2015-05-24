from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from apps.cursos.models import LeaderTeacher, Curso, Cohorte
from logica.estudiante import Estudiante

import json


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
	
	if request.method == "POST":
		id_curso = request.POST.get('id_curso')
		curso = Curso.objects.get(id=id_curso)

		cohortes = Cohorte.objects.filter(curso_id=id_curso)
		
		estudiantes = []
		
		for cohorte in cohortes:
			leader_teachers = LeaderTeacher.objects.filter(cohorte__id=cohorte.id)
			for leader_teacher in leader_teachers:
				estudiantes.append(leader_teacher)
		
		
		contexto = {'curso': curso,'estudiantes':estudiantes}
		return render_to_response('tabla3.html',contexto,context_instance= RequestContext(request))
		
	else:
		cursos = Curso.objects.all()
		contexto = {'cursos': cursos}
		return render_to_response('tabla3_consulta.html',contexto,context_instance= RequestContext(request))
		
def reporte_cursos_numero_asitentes(request):

	#Datos Bar chart
	labels = ["enero", "febrero", "Marzo"]
	json_labels = json.dumps(labels)
	datos = [100, 5, 7]
	

	#Datos Donut chart
	labels_doughnut_chart = ["Curso 1","Curso 2","Curso 3"]
	json_labels_doughnut_chart = json.dumps(labels_doughnut_chart)

	colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
	"#F6CEF5","#04B486","#F7D358"]
	json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

	datos_doughnut_chart = [80,20,20]

	contexto = {
	'datos': datos, 
	'labels': json_labels,
	'datos_doughnut':datos_doughnut_chart,
	'labels_doughnut':json_labels_doughnut_chart,
	'colors_doughnut':json_colors_doughnut_chart}
	return render_to_response('grafica1.html', contexto, context_instance= RequestContext(request))
