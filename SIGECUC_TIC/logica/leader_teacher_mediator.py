from django.template import RequestContext
from django.shortcuts import render_to_response

#from .forms import Persona_MasterTeacherForm
from apps.cursos.forms import Informacion_personalForm
from apps.cursos.models import LeaderTeacher
from apps.cursos.models import Cursos_Inscrito
from apps.cursos.models import Calificacion
from apps.cursos.models import Cohorte

#Esta clase representa una tarea, que envuelve todas las acciones 
#necesarias para llevar a cabo la tarea
class InformacionPersonalTask:

	#Funcion que despliega la informacion personal del usuario
	def get_informacion_personal(self,request):
		user = request.user
		user_id = user.id
		#consulta a Mater Teacher
		leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
		form_personaLeaderTeacher = Informacion_personalForm(request.POST, instance= leader_teacher) 

		form_personaLeaderTeacher = Informacion_personalForm(initial = {'identificacion' : leader_teacher.inscrito.persona.identificacion, 
			'primer_nombre' : leader_teacher.inscrito.persona.primer_nombre, 'segundo_nombre' : leader_teacher.inscrito.persona.segundo_nombre,
			'primer_apellido': leader_teacher.inscrito.persona.primer_apellido, 'segundo_apellido' : leader_teacher.inscrito.persona.segundo_apellido,
			'email' : leader_teacher.inscrito.persona.email, 'telefono' : leader_teacher.inscrito.persona.telefono, 
			'direccion' : leader_teacher.inscrito.persona.direccion

			})
		contexto = {'user':user, 'form_personaLeaderTeacher' : form_personaLeaderTeacher}
		return render_to_response('leader_teacher_informacion_personal.html',contexto, context_instance= RequestContext(request))
		
				
	#Funcion para actualizar la infomarmacion personal
	def update_informacion_personal(self,request):
		if self.informacion_personal_form_valid(request):
			#Si el formulario es valido entonces se guarda en la base de datos
			return self.save_informacion_personal_form(request)
		else:
			#Si no es valido entonces se muestran los errores
			return self.get_informacion_personal_form_invalid(request)

	#Permite validar el formulario de informacion personal
	def informacion_personal_form_valid(self,request):
		user = request.user
		user_id = user.id
		leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
		#se instancia el master_teacher para que pase la validez y sea un formulario para modificar
		form_personaLeaderTeacher = Informacion_personalForm(request.POST, instance=leader_teacher)
		return form_personaLeaderTeacher.is_valid()

	#En caso de que el formulario de informacion personal no sea valido
	#Se muestra el formulario con los errores
	def get_informacion_personal_form_invalid(self,request):
		form_personaLeaderTeacher = Informacion_personalForm(request.POST)
		contexto = {
		'form_personaLeaderTeacher':form_personaLeaderTeacher,
		'user':user }
		return render_to_response('leader_teacher.html',contexto)

	#Si el formulario es valido , entonces se actualiza la informacion en la base de datos
	def save_informacion_personal_form(self,request):
		user = request.user
		user_id = user.id
		leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
		#se instancia el master_teacher para que pase la validez y sea un formulario para modificar
		form_personaLeaderTeacher = Informacion_personalForm(request.POST, instance=leader_teacher)
		form_personaLeaderTeacher.is_valid()
		email = form_personaLeaderTeacher.cleaned_data["email"]
		leader_teacher.inscrito.persona.email = email
		telefono = form_personaLeaderTeacher.cleaned_data["telefono"]
		leader_teacher.inscrito.persona.telefono = telefono
		direccion = form_personaLeaderTeacher.cleaned_data["direccion"]
		leader_teacher.inscrito.persona.direccion = direccion
		leader_teacher.inscrito.persona.save()
		titulo = "Su informacion personal ha sido modificada correctamente"
		
		contexto = {
		'user':user,
		'titulo':titulo}
		return render_to_response('leader_teacher.html',contexto)

class CalificacionesTask:

	def get_cursos_calificados(self,request):
		user = request.user
		user_id = user.id
		#Se busca la identificacion del Leader Teacher
		leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
		contexto = {'user': user, 'leader_teacher': leader_teacher}
		return render_to_response('leader_teacher_calificaciones.html', contexto, context_instance = RequestContext(request))

	def get_detalle_calificacion_curso(self,request,cohorte_id):
		#https://docs.djangoproject.com/en/1.8/topics/db/aggregation/
		#funcion que permite ver las calificaciones de el curso actual
		user = request.user
		user_id = user.id
		#id_cohorte = request.GET.get('id_cohorte')
		

		cohorte = Cohorte.objects.get(id=cohorte_id)
		curso_id = cohorte.curso.id

		#Se busca la identificacion del Leader Teacher
		leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
		id_leader_teacher = leader_teacher.inscrito.persona.identificacion

		#se busca el curso que pertenece el inscrito
		curso_inscrito = Cursos_Inscrito.objects.get(inscrito_id=id_leader_teacher,curso__id=curso_id)
		#Se busca las calificaciones ordenando por attividad
		calificaciones = Calificacion.objects.filter(leader_teacher_id=id_leader_teacher, cohorte_id=cohorte_id).order_by('actividad_id')
		#usa fiuncion para calcular la nota_final
		nota_final = self.calcular_nota_final_curso(calificaciones)
		aprobo = self.validar_aprobacion(nota_final)
		contexto = {'user':user, 'curso_inscrito': curso_inscrito, 'calificaciones': calificaciones, 'nota_final': nota_final, 'aprobo':aprobo }
		return render_to_response('leader_teacher_descripcion_calificacion.html',contexto, context_instance= RequestContext(request))


	def validar_aprobacion(self,nota):
		#valida si aprobo o no el estudiante
		aprobo = False
		if nota >= 3:
			aprobo = True
		return aprobo


	def calcular_nota_final_curso(self,calificaciones):
		nota_final = 0.0
		#funcion que calcula la nota final del curso con su peso en porcentaje
		for calificacion in calificaciones:
			nota_parcial = float(calificacion.nota_actividad)
			porcentaje_actividad = float(calificacion.actividad.peso)
			nota_final = nota_final + (nota_parcial * porcentaje_actividad)
		return nota_final

class LeaderTeacherMediator:

	#Tarea relacionada con la informacion personal
	def informacion_personal_task(self,request,option=1):
		leader_teacher_informacion_personal_task = InformacionPersonalTask()
		if option == 1:
			return leader_teacher_informacion_personal_task.get_informacion_personal(request)
		else:
			return leader_teacher_informacion_personal_task.update_informacion_personal(request)

	def calificaciones_task(self,request,cohorte_id=None,option=1):
		leader_teacher_calificacion_task = CalificacionesTask()
		if option == 1:
			return leader_teacher_calificacion_task.get_cursos_calificados(request)
		else:
			return leader_teacher_calificacion_task.get_detalle_calificacion_curso(request,cohorte_id)




