from Observable import Observable
from ReporteCurso import ReporteCurso
from ReporteLeaderTeacher import ReporteLeaderTeacher

class Reporte(Observable):

	def __init__(self):
		self.reporteCurso = ReporteCurso()
		self.reporteLeaderTeacher = ReporteLeaderTeacher()
		self.observadores = []

	def registrar(self,observador):
		if observador not in self.observadores:
			self.observadores.append(observador)

	def anular(self,observador):
		self.observadores.remove(observador)

	def notificarTodos(self):
		for objeto in self.observadores:
			objeto.update(self,self.reporteCurso,self.reporteLeaderTeacher)

	def getCursoMayorNumeroAsistentes(self,periodo,tipo):
		if tipo == "mes":
			pass
		elif tipo == "semestre":
			pass

	def getNumeroLeaderTeachersNuevosPorDepartamento(self,periodo,tipo):
		if tipo == "mes":
			pass
		elif tipo == "semestre":
			pass

	def getCursosConMenorPotenciaAvance(self,periodo,tipo):
		if tipo == "mes":
			pass
		elif tipo == "semestre":
			pass

	def getPorcentajeLeaderTeacherAprobaronCursos(self,periodo,tipo,departamentos):
		if tipo == "mes":
			pass
		elif tipo == "semestre":
			pass

	def getPorcentajeLeaderTeacherReporbaronCursos(self,periodo,tipo,departamentos):
		if tipo == "mes":
			pass
		elif tipo == "semestre":
			pass
	def getDetalleReportesNotasPorEstudiante(self,mes):
		pass

	def getDetalleEstudiantesEnCursos(self,mes,departamentos):
		pass

	def update():
		pass

			