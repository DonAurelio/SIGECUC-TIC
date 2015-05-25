from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from apps.cursos.models import LeaderTeacher, Curso, Cohorte, Asistencia, Inscrito
from logica.estudiante import Estudiante
from django.db.models import Count

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
		
#=======================>Inicio grafica1<============================================================		
def reporte_cursos_numero_asitentes(request):
	fechas_distintas = Asistencia.objects.all().distinct('mes','anio')
	fechas_disponibles = []
	for asistencia in fechas_distintas:
		fechas_disponibles.append(asistencia.mes + "/" + asistencia.anio)

	if request.method == "POST":

		#Inicio grafica de barras
		fecha = request.POST.get('id_fecha')
		mes_anio = fecha.split('/')
		mes = mes_anio[0]
		anio = mes_anio[1]

		cursos_asistencias = Asistencia.objects.filter(mes=mes,anio=anio).distinct('cohorte__curso__nombre')
		numero_asistentes = []
		
		for asistente in cursos_asistencias:
			asistentes_curso = Asistencia.objects.filter(mes=mes,anio=anio,cohorte__curso__nombre=asistente.cohorte.curso.nombre).distinct('leader_teacher__inscrito__persona__identificacion')
			numero_asistentes.append(len(asistentes_curso))

		labels_bar = []
		datos_bar = []
		
		for asistente, numero in zip(cursos_asistencias,numero_asistentes):
			labels_bar.append(asistente.cohorte.curso.nombre)
			datos_bar.append(numero)
		
		json_labels_bar = json.dumps(labels_bar)
		#Fin grafica de barras

		#Inicio grafica dona
		labels_doughnut_chart = ["Curso 1","Curso 2","Curso 3"]
		json_labels_doughnut_chart = json.dumps(labels_doughnut_chart)

		colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
		"#F6CEF5","#04B486","#F7D358"]
		json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

		datos_doughnut_chart = [80,20,20]
		#Fin grafica dona


		contexto = {
		'labels_bar':json_labels_bar, 
		'datos_bar':datos_bar,
		'datos_doughnut':datos_bar,
		'labels_doughnut':json_labels_bar,
		'colors_doughnut':json_colors_doughnut_chart,
		'fechas_disponibles':fechas_disponibles

		}

		return render_to_response('grafica1.html', contexto, context_instance= RequestContext(request))

	else:
		
		
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
		'fechas_disponibles':fechas_disponibles,
		'datos_bar': datos, 
		'labels_bar': json_labels,
		'datos_doughnut':datos_doughnut_chart,
		'labels_doughnut':json_labels_doughnut_chart,
		'colors_doughnut':json_colors_doughnut_chart}
		return render_to_response('grafica1.html', contexto, context_instance= RequestContext(request))

#=======================>FIN grafica1<============================================================	


#================================== INICIO grafica 2 =============================================
def reporte_docentes_estudiantes_departamento(request):
	fechas_distintas = LeaderTeacher.objects.all().distinct('mes','anio')
	fechas_disponibles = []
	for asistencia in fechas_distintas:
		fechas_disponibles.append(asistencia.mes + "/" + asistencia.anio)

	if request.method == "POST":

		#Inicio grafica de barras
		fecha = request.POST.get('id_fecha')
		mes_anio = fecha.split('/')
		mes = mes_anio[0]
		anio = mes_anio[1]


		leader_teachers_departamentos = LeaderTeacher.objects.filter(mes=mes,anio=anio).distinct('departamento_labora')
		numero_leader_teachers = []
		
		for leader_teachers_departamento in leader_teachers_departamentos:
			departamento = leader_teachers_departamento.departamento_labora
			leader_teachers = LeaderTeacher.objects.filter(mes=mes,anio=anio,departamento_labora=departamento)
			numero_leader_teachers.append(len(leader_teachers))
			
		labels_bar = []
		datos_bar = []
		
		for leader_teacher, numero in zip(leader_teachers_departamentos,numero_leader_teachers):
			labels_bar.append(leader_teacher.departamento_labora)
			datos_bar.append(numero)
		
		json_labels_bar = json.dumps(labels_bar)
		#Fin grafica de barras

		#Inicio grafica dona
		labels_doughnut_chart = ["Curso 1","Curso 2","Curso 3"]
		json_labels_doughnut_chart = json.dumps(labels_doughnut_chart)

		colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
		"#F6CEF5","#04B486","#F7D358"]
		json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

		datos_doughnut_chart = [80,20,20]
		#Fin grafica dona


		contexto = {
		'labels_bar':json_labels_bar, 
		'datos_bar':datos_bar,
		'datos_doughnut':datos_bar,
		'labels_doughnut':json_labels_bar,
		'colors_doughnut':json_colors_doughnut_chart,
		'fechas_disponibles':fechas_disponibles

		}

		return render_to_response('grafica2.html', contexto, context_instance= RequestContext(request))

	else:
		
		
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
		'fechas_disponibles':fechas_disponibles,
		'datos_bar': datos, 
		'labels_bar': json_labels,
		'datos_doughnut':datos_doughnut_chart,
		'labels_doughnut':json_labels_doughnut_chart,
		'colors_doughnut':json_colors_doughnut_chart}
		return render_to_response('grafica2.html', contexto, context_instance= RequestContext(request))


#=======================>FIN grafica 2<============================================================	

def reporte_cursos_menor_potencial_avance(request):
	cursos = Curso.objects.all()
	notas_finales_estudiantes = 0
	nota_cohortes = 0
	notas_cursos = []
	a = ""
	for curso in cursos:
		cohortes = Cohorte.objects.filter(curso_id=curso.id)
		for cohorte in cohortes:
			nota_cohortes = 0
			notas_finales_estudiantes = 0
			leader_teachers = LeaderTeacher.objects.filter(cohorte__id=cohorte.id)
			for leader_teacher in leader_teachers:
				estudiante = Estudiante(leader_teacher)
				nota_final = estudiante.calcular_nota_final_cohorte(cohorte)
				notas_finales_estudiantes += nota_final
				a += leader_teacher.inscrito.persona.primer_nombre + "/" + cohorte.curso.nombre +"/"+ str(nota_final) +"<br>"
			nota_cohortes += notas_finales_estudiantes / len(leader_teachers)
		notas_cursos.append(nota_cohortes)
	
	labels_bar = []
	datos_bar = []
	
	for curso, nota in zip(cursos,notas_cursos):
		labels_bar.append(curso.nombre)
		datos_bar.append(nota)
	
	json_labels_bar = json.dumps(labels_bar)
	#Fin grafica de barras

	#Inicio grafica dona
	labels_doughnut_chart = ["Curso 1","Curso 2","Curso 3"]
	json_labels_doughnut_chart = json.dumps(labels_doughnut_chart)

	colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
	"#F6CEF5","#04B486","#F7D358"]
	json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

	datos_doughnut_chart = [80,20,20]
	#Fin grafica dona


	contexto = {
	'labels_bar':json_labels_bar, 
	'datos_bar':datos_bar,
	'datos_doughnut':datos_bar,
	'labels_doughnut':json_labels_bar,
	'colors_doughnut':json_colors_doughnut_chart,
	
	}

	return render_to_response('grafica3.html', contexto, context_instance= RequestContext(request))

	
