from apps.cursos.models import Calificacion

class Estudiante:
	def __init__(self,estudiante):
		self.estudiante = estudiante
		self.cohortes = estudiante.cohorte.all()
		self.calcular_nota_final()
		self.calcular_cohortes_cursos_aprobadas()
		self.aprobo_un_curso()


	def calcular_nota_final(self):
		calificacines_finales = []
		for cohorte in self.cohortes:
			calificaciones = Calificacion.objects.filter(cohorte_id=cohorte.id,leader_teacher_id=self.estudiante.inscrito.persona.identificacion)
			nota_final = self.calcular_nota_final_curso(calificaciones)
			calificacines_finales.append(nota_final)
			
		self.cohortes_calificaciones = zip(self.cohortes,calificacines_finales)

	def aprobo_un_curso(self):
		self.aprobo_almenos_un_curso = True
		if self.cohortes_aprobadas == []:
			self.aprobo_almenos_un_curso = False


	def calcular_cohortes_cursos_aprobadas(self):
		self.cohortes_aprobadas = []
		for cohorte , calificacion_final in self.cohortes_calificaciones:
			if calificacion_final >= 3.0:
				self.cohortes_aprobadas.append(cohorte)
				
	
	def calcular_nota_final_curso(self,calificaciones):
		nota_final = 0.0
		#funcion que calcula la nota final del curso con su peso en porcentaje
		for calificacion in calificaciones:
			nota_parcial = float(calificacion.nota_actividad)
			porcentaje_actividad = float(calificacion.actividad.peso)
			nota_final += (nota_parcial * porcentaje_actividad)
		return nota_final


			
		

