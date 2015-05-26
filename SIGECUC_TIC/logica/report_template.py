
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from apps.cursos.models import LeaderTeacher, Curso, Cohorte, Asistencia, Inscrito
from logica.estudiante import Estudiante
from django.db.models import Count

import json

class ReportTemplate:
	def get_report(self,request):
		pass

class NotasPorEstudiantesReport(ReportTemplate):

	def get_report(self,request):
		user = request.user
		estudiantes = LeaderTeacher.objects.all()
		estudiantes_calificados = []
		for estudiante in estudiantes:
			estudiantes_calificados.append(Estudiante(estudiante))
		
		contexto = {'user':user,'estudiantes':estudiantes_calificados}

		return render_to_response('tabla1.html',contexto)


class EstudiantesCursosAprobadosReport(ReportTemplate):

	def get_report(self,request):
		user = request.user
		leader_teachers = LeaderTeacher.objects.all()
		estudiantes_curso_aprobado = []
		for leader_teacher in leader_teachers:
			estudiante = Estudiante(leader_teacher)
			if estudiante.aprobo_almenos_un_curso:
				estudiantes_curso_aprobado.append(estudiante)
		
		contexto = {'user':user,'estudiantes':estudiantes_curso_aprobado}

		return render_to_response('tabla2.html',contexto)

class EstudiantesPorCursosPorDepartamentoReport(ReportTemplate):

	def get_report(self,request):
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

#===========================================================================================================================

#===========================================================================================================================


class GraphTemplate:

	def __init__(self):
		self.labels = None
		self.data = None
		self.title_graph = None
		self.filter_title = None
		self.filter_items = None
		self.colors_doughnut = [
		"#F7464A","#46BFBD","#FDB45C","#F3E2A9","#8181F7",
		"#FFBF00","#01DFD7","#F6CEF5","#04B486","#F7D358"]
		self.title_message = None
		self.message = None

	def get_presentation(self,request):
		
		self.labels = ["Enero", "Febrero", "Marzo"]
		self.data = [100, 5, 7]
		
		contexto = {
		'title_message':self.title_message,
		'message':self.message,
		'title_graph':self.title_graph,
		'filter_title':filter_title,
		'filter_items':self.filter_items,
		'labels': json.dumps(self.labels),
		'data': self.data, 
		'colors_doughnut':json.dumps(self.colors_doughnut)

		}
		return render_to_response('grafica.html', contexto, context_instance= RequestContext(request))

	def get_graph(self,request):

		contexto = {
		'title_message':self.title_message,
		'message':self.message,
		'title_graph':self.title_graph,
		'filter_title':filter_title,
		'filter_items':self.filter_items,
		'labels': json.dumps(self.labels),
		'data': self.data, 
		'colors_doughnut':json.dumps(self.colors_doughnut)

		}
		return render_to_response('grafica.html', contexto, context_instance= RequestContext(request))
				
	def get_data(self,request):
		pass

class CursoMayorNumeroAsistentesGraph(GraphTemplate):

	def __init__(self):
		GraphTemplate.__init__(self)

	def get_data(self,request):
		pass