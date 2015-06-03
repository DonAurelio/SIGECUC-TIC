from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from apps.cursos.models import LeaderTeacher, Curso, Cohorte, Asistencia, Inscrito, Persona
from logica.estudiante import Estudiante
from django.db.models import Count

import json

from logica.report_template import NotasPorEstudiantesReport
from logica.report_template import EstudiantesCursosAprobadosReport
from logica.report_template import EstudiantesPorCursosPorDepartamentoReport
from logica.report_template import GraphTemplate

#@login_required(login_url='login/')	
def principal(request):
	user = request.user
	
	titulo = "Bienvenid@ al modulo de reportes, " + user.username
	mensaje = """ Aqui podras visualizar Tablas y Graficos estadisticos hacerca 
	de la informacion mas relevante del sistema SIGECUC-TIC, relacionado con cursos
	y estudiantes"""
		
	contexto = {
	'titulo':titulo,
	'mensaje':mensaje}
	return render_to_response('principal.html',contexto, context_instance=RequestContext(request))

#=================================================================================================

#@login_required(login_url='login/')	
def reporte_notas_por_estudiantes(request):
	reporte1 = NotasPorEstudiantesReport()
	return reporte1.get_report(request)
	
def reporte_estudiantes_cursos_aprobados(request):
	reporte2 = EstudiantesCursosAprobadosReport()
	return reporte2.get_report(request)
	
def reporte_estudiantes_curso_por_departamento(request):
	reporte3 = EstudiantesPorCursosPorDepartamentoReport()
	return reporte3.get_report(request)
		
#=================================================================================================

def reporte_cursos_numero_asitentes(request):
	

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

		labels = []
		data = []
		
		for asistente, numero in zip(cursos_asistencias,numero_asistentes):
			labels.append(asistente.cohorte.curso.nombre)
			data.append(numero)
		
		json_labels = json.dumps(labels)
		#Fin grafica de barras

		#Inicio grafica dona
		
		colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
		"#F6CEF5","#04B486","#F7D358"]
		json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)
		
		#Fin grafica dona

		fechas_distintas = Asistencia.objects.all().distinct('mes','anio')
		fechas_disponibles = []
		for asistencia in fechas_distintas:
			fechas_disponibles.append(asistencia.mes + "/" + asistencia.anio)

		title_graph = "Graficas cursos mayor numero asistentes "
		filter_label = "Por favor seleccione el mes que desea consultar"
		contexto = {
		'title_graph': title_graph,
		'filter_label': filter_label,
		'filter_items': fechas_disponibles,
		'labels':json_labels, 
		'data':data,
		'colors_doughnut':json_colors_doughnut_chart,
		}

		return render_to_response('grafica.html', contexto, context_instance= RequestContext(request))

	else:
		fechas_distintas = Asistencia.objects.all().distinct('mes','anio')
		fechas_disponibles = []
		for asistencia in fechas_distintas:
			fechas_disponibles.append(asistencia.mes + "/" + asistencia.anio)
		
		
		#Datos Bar chart
		labels = ["Ejemplo 1", "Ejemplo 2", "Ejemplo 3"]
		json_labels = json.dumps(labels)
		data = [100, 5, 7]
		

		#Datos Donut chart
		colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
		"#F6CEF5","#04B486","#F7D358"]
		json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

		
		title_graph = "Graficas cursos mayor numero asistentes "
		filter_label = "Por favor seleccione el mes que desea consultar"
		contexto = {
		'title_graph': title_graph,
		'filter_label': filter_label,
		'filter_items': fechas_disponibles,
		'labels':json_labels, 
		'data':data,
		'colors_doughnut':json_colors_doughnut_chart,
		}
		return render_to_response('grafica.html', contexto, context_instance= RequestContext(request))


def reporte_docentes_estudiantes_departamento(request):
	
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
			
		labels = []
		data = []
		
		for leader_teacher, numero in zip(leader_teachers_departamentos,numero_leader_teachers):
			labels.append(leader_teacher.departamento_labora)
			data.append(numero)
		
		json_labels = json.dumps(labels)
		#Fin grafica de barras

		#Inicio grafica dona
		
		colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
		"#F6CEF5","#04B486","#F7D358"]
		json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

		datos_doughnut_chart = [80,20,20]
		#Fin grafica dona

		fechas_distintas = LeaderTeacher.objects.all().distinct('mes','anio')
		fechas_disponibles = []
		for asistencia in fechas_distintas:
			fechas_disponibles.append(asistencia.mes + "/" + asistencia.anio)


		title_graph = "Estudiantes que han llegado por departamento en el mes"
		filter_label = "Por favor seleccione el mes que desea consultar"
		contexto = {
		'title_graph': title_graph,
		'filter_label': filter_label,
		'filter_items': fechas_disponibles,
		'labels':json_labels, 
		'data':data,
		'colors_doughnut':json_colors_doughnut_chart,
		}
		return render_to_response('grafica.html', contexto, context_instance= RequestContext(request))
	else:

		fechas_distintas = LeaderTeacher.objects.all().distinct('mes','anio')
		fechas_disponibles = []
		for asistencia in fechas_distintas:
			fechas_disponibles.append(asistencia.mes + "/" + asistencia.anio)
		
		
		#Datos Bar chart
		labels = ["Ejemplo 1", "Ejemplo 2", "Ejemplo 3"]
		json_labels = json.dumps(labels)
		data = [100, 5, 7]
		

		#Datos Donut chart
		colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
		"#F6CEF5","#04B486","#F7D358"]
		json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

		
		title_graph = "Estudiantes que han llegado por departamento en el mes"
		filter_label = "Por favor seleccione el mes que desea consultar"
		contexto = {
		'title_graph': title_graph,
		'filter_label': filter_label,
		'filter_items': fechas_disponibles,
		'labels':json_labels, 
		'data':data,
		'colors_doughnut':json_colors_doughnut_chart,
		}
		return render_to_response('grafica.html', contexto, context_instance= RequestContext(request))

#=======================>FIN grafica 2<============================================================	

def reporte_cursos_menor_potencial_avance(request):
	cursos = Curso.objects.all()
	notas_finales_estudiantes = 0
	nota_cohortes = 0
	notas_cursos = []
	a = ""
	c = ""
	for curso in cursos:
		nota_cohortes = 0
		notas_finales_estudiantes = 0
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
	
	labels = []
	data = []
	
	for curso, nota in zip(cursos,notas_cursos):
		labels.append(curso.nombre)
		data.append(nota)
	
	json_labels = json.dumps(labels)
	#Fin grafica de barras

	#Datos Donut chart
	colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
	"#F6CEF5","#04B486","#F7D358"]
	json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

	#Inicio grafica dona
	title_graph = "Cursos menor potencial de avance Top(5)"
	contexto = {
	'title_graph': title_graph,
	'labels':json_labels, 
	'data':data,
	'colors_doughnut':json_colors_doughnut_chart,
	}
	return render_to_response('grafica.html', contexto, context_instance= RequestContext(request))

	
#================================== INICIO grafica 2 =============================================

def reporte_porcentaje_estudiantes_aprobados_cursos_departamentos(request):

	cursos_disponibles = []
	leader_teachers = LeaderTeacher.objects.all().distinct('cohorte__curso__nombre')
	departametos_disponibles = []
	for leader_teacher in leader_teachers:
		cohortes = leader_teacher.cohorte.all().distinct('curso__nombre')
		for cohorte in cohortes:
			cursos_disponibles.append(cohorte.curso)

	if request.method == "POST":

		id_curso = request.POST.get('id_curso')
		cohortes = Cohorte.objects.filter(curso_id=id_curso)
		departamentos = []
		for cohorte in cohortes:
			leader_teachers = LeaderTeacher.objects.filter(cohorte__id=cohorte.id).distinct('departamento_labora')
			for leader_teacher in leader_teachers:
				departamentos.append(leader_teacher.departamento_labora)

		aprobados_departamentos = []
		for cohorte in cohortes:
			for departamento in departamentos:
				numero_aprobados_cohorte = 0
				leader_teachers = LeaderTeacher.objects.filter(cohorte__id=cohorte.id,departamento_labora=departamento)
				for leader_teacher in leader_teachers:
					estudiante = Estudiante(leader_teacher)
					nota_final = estudiante.calcular_nota_final_cohorte(cohorte)
					if nota_final >= 3.0:
						numero_aprobados_cohorte += 1
				aprobados_departamentos.append(numero_aprobados_cohorte)


			
		labels_bar = []
		datos_bar = []
		
		for departamento, numero in zip(departamentos,aprobados_departamentos):
			labels_bar.append(departamento)
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

		graph_title = "Porcentaje de estudiantes que aprobaron un curso por departamento"

		contexto = {
		'graph_title': graph_title,
		'labels_bar':json_labels_bar, 
		'datos_bar':datos_bar,
		'datos_doughnut':datos_bar,
		'labels_doughnut':json_labels_bar,
		'colors_doughnut':json_colors_doughnut_chart,
		'cursos_disponibles':cursos_disponibles

		}

		return render_to_response('grafica_procentaje.html', contexto, context_instance= RequestContext(request))

	else:
		
		
		labels = ["Ejemplo 1", "Ejemplo 2", "Ejemplo 3"]
		json_labels = json.dumps(labels)
		data = [100, 5, 7]
		
	
		colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
		"#F6CEF5","#04B486","#F7D358"]
		json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)


		graph_title = "Porcentaje de estudiantes que aprobaron un curso por departamento"
	
		contexto = {
		'graph_title':graph_title,
		'cursos_disponibles':cursos_disponibles,
		'datos_bar': data, 
		'labels_bar': json_labels,
		'datos_doughnut':data,
		'labels_doughnut':json_labels,
		'colors_doughnut':json_colors_doughnut_chart

		}
		return render_to_response('grafica_procentaje.html', contexto, context_instance= RequestContext(request))

def reporte_porcentaje_estudiantes_reprobados_cursos_departamentos(request):
	cursos_disponibles = []
	leader_teachers = LeaderTeacher.objects.all().distinct('cohorte__curso__nombre')
	departametos_disponibles = []
	for leader_teacher in leader_teachers:
		cohortes = leader_teacher.cohorte.all().distinct('curso__nombre')
		for cohorte in cohortes:
			cursos_disponibles.append(cohorte.curso)

	if request.method == "POST":

		id_curso = request.POST.get('id_curso')
		cohortes = Cohorte.objects.filter(curso_id=id_curso)
		departamentos = []
		for cohorte in cohortes:
			leader_teachers = LeaderTeacher.objects.filter(cohorte__id=cohorte.id).distinct('departamento_labora')
			for leader_teacher in leader_teachers:
				departamentos.append(leader_teacher.departamento_labora)

		aprobados_departamentos = []
		for cohorte in cohortes:
			for departamento in departamentos:
				numero_aprobados_cohorte = 0
				leader_teachers = LeaderTeacher.objects.filter(cohorte__id=cohorte.id,departamento_labora=departamento)
				for leader_teacher in leader_teachers:
					estudiante = Estudiante(leader_teacher)
					nota_final = estudiante.calcular_nota_final_cohorte(cohorte)
					if nota_final < 3.0:
						numero_aprobados_cohorte += 1
				aprobados_departamentos.append(numero_aprobados_cohorte)


			
		labels_bar = []
		datos_bar = []
		
		for departamento, numero in zip(departamentos,aprobados_departamentos):
			labels_bar.append(departamento)
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

		graph_title = "Porcentaje de estudiantes que reprobaron un curso por departamento"

		contexto = {
		'graph_title':graph_title,
		'labels_bar':json_labels_bar, 
		'datos_bar':datos_bar,
		'datos_doughnut':datos_bar,
		'labels_doughnut':json_labels_bar,
		'colors_doughnut':json_colors_doughnut_chart,
		'cursos_disponibles':cursos_disponibles

		}

		return render_to_response('grafica_procentaje.html', contexto, context_instance= RequestContext(request))

	else:
		
		
		labels = ["Ejemplo 1", "Ejemplo 2", "Ejemplo 3"]
		json_labels = json.dumps(labels)
		data = [100, 5, 7]
		
	
		colors_doughnut_chart = ["#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7","#FFBF00","#01DFD7",
		"#F6CEF5","#04B486","#F7D358"]
		json_colors_doughnut_chart = json.dumps(colors_doughnut_chart)

		graph_title = "Porcentaje de estudiantes que reprobaron un curso por departamento"
	
		contexto = {
		'graph_title':graph_title,
		'cursos_disponibles':cursos_disponibles,
		'datos_bar': data, 
		'labels_bar': json_labels,
		'datos_doughnut':data,
		'labels_doughnut':json_labels,
		'colors_doughnut':json_colors_doughnut_chart

		}
		return render_to_response('grafica_procentaje.html', contexto, context_instance= RequestContext(request))