from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User

#from .forms import Persona_MasterTeacherForm
from apps.cursos.forms import Informacion_personalForm
from apps.cursos.models import LeaderTeacher
from apps.cursos.models import Cursos_Inscrito
from apps.cursos.models import Calificacion

# Create your views here.

#=========================> Inicio pagina_leader_teacher_informacion_personal #=========================>
def pagina_leader_teacher_informacion_personal(request):
	#Funcion que muestra el formulario para modificar datos presonales
	user = request.user
	user_id = user.id
	#consulta a Mater Teacher
	leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
	if request.method == "POST":
		#se instancia el master_teacher para que pase la validez y sea un formulario para modificar
		form_personaLeaderTeacher = Informacion_personalForm(request.POST, instance=leader_teacher)
		if form_personaLeaderTeacher.is_valid():
			email = form_personaLeaderTeacher.cleaned_data["email"]
			leader_teacher.inscrito.persona.email = email
			telefono = form_personaLeaderTeacher.cleaned_data["telefono"]
			leader_teacher.inscrito.persona.telefono = telefono
			direccion = form_personaLeaderTeacher.cleaned_data["direccion"]
			leader_teacher.inscrito.persona.direccion = direccion
			leader_teacher.inscrito.persona.save()
			mensaje = "Su informacion personal ha sido modificada correctamente"
			return render_to_response('leader_teacher.html',{'user':user,'mensaje':mensaje})
	
	else:
		form_personaLeaderTeacher = Informacion_personalForm(request.POST, instance= leader_teacher) 

		form_personaLeaderTeacher = Informacion_personalForm(initial = {'identificacion' : leader_teacher.inscrito.persona.identificacion, 
			'primer_nombre' : leader_teacher.inscrito.persona.primer_nombre, 'segundo_nombre' : leader_teacher.inscrito.persona.segundo_nombre,
			'primer_apellido': leader_teacher.inscrito.persona.primer_apellido, 'segundo_apellido' : leader_teacher.inscrito.persona.segundo_apellido,
			'email' : leader_teacher.inscrito.persona.email, 'telefono' : leader_teacher.inscrito.persona.telefono, 
			'direccion' : leader_teacher.inscrito.persona.direccion

			})
	contexto = {'user':user, 'form_personaLeaderTeacher' : form_personaLeaderTeacher}
	return render_to_response('leader_teacher_informacion_personal.html',contexto, context_instance= RequestContext(request))
#=========================> FIN pagina_leader_teacher_informacion_personal #=========================>



#=========================> Inicio pagina_leader_teacher_calificaciones #=========================>

def validar_aprobacion(nota):
	#valida si aprobo o no el estudiante
	aprobo = False
	if nota >= 3:
		aprobo = True
	return aprobo


def calcular_nota_final_curso(calificaciones):
	nota_final = 0.0
	#funcion que calcula la nota final del curso con su peso en porcentaje
	for calificacion in calificaciones:
		nota_parcial = float(calificacion.nota_actividad)
		porcentaje_actividad = float(calificacion.actividad.peso)
		nota_final = nota_final + (nota_parcial * porcentaje_actividad)
	return nota_final



def pagina_leader_teacher_descripcion_calificacion(request):
	#https://docs.djangoproject.com/en/1.8/topics/db/aggregation/
#funcion que permite ver las calificaciones de el curso actual
	user = request.user
	user_id = user.id
	id_cohorte = request.GET.get('id_cohorte')
	
	#Se busca la identificacion del Leader Teacher
	leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
	id_leader_teacher = leader_teacher.inscrito.persona.identificacion

	#se busca el curso que pertenece el inscrito
	curso_inscrito = Cursos_Inscrito.objects.get(inscrito_id=id_leader_teacher)
	#Se busca las calificaciones ordenando por attividad
	calificaciones = Calificacion.objects.filter(leader_teacher_id=id_leader_teacher, cohorte_id=id_cohorte).order_by('actividad_id')
	#usa fiuncion para calcular la nota_final
	nota_final = calcular_nota_final_curso(calificaciones)
	aprobo = validar_aprobacion(nota_final)
	contexto = {'user':user, 'curso_inscrito': curso_inscrito, 'calificaciones': calificaciones, 'nota_final': nota_final, 'aprobo':aprobo }
	return render_to_response('leader_teacher_descripcion_calificacion.html',contexto, context_instance= RequestContext(request))


def pagina_consulta_cursos_calificados(request):

#funcion que permite ver las calificaciones de el curso actual
	user = request.user
	user_id = user.id
	#Se busca la identificacion del Leader Teacher
	leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
	contexto = {'user': user, 'leader_teacher': leader_teacher}
	return render_to_response('leader_teacher_calificaciones.html', contexto, context_instance = RequestContext(request))



#=========================> FIN pagina_leader_teacher_calificaciones #=========================>
