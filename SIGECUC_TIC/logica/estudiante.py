from apps.cursos.models import Calificacion

class Estudiante:
	def __init__(self,estudiante):
		self.estudiante = estudiante
		self.cohortes = estudiante.cohorte.all()
		self.calificacines_finales = []
		for cohorte in self.cohortes:
			calificaciones = Calificacion.objects.filter(cohorte_id=cohorte.id,leader_teacher_id=self.estudiante.inscrito.persona.identificacion)
			self.calificacines_finales.append(self.calcular_nota_final_curso(calificaciones))
		self.cohortes_calificaciones = zip(self.cohortes,self.calificacines_finales)

	def calcular_nota_final_curso(self,calificaciones):
		 nota_final = 0.0
		 #funcion que calcula la nota final del curso con su peso en porcentaje
		 for calificacion in calificaciones:
			nota_parcial = float(calificacion.nota_actividad)
			porcentaje_actividad = float(calificacion.actividad.peso)
			nota_final += (nota_parcial * porcentaje_actividad)
		 return nota_final

