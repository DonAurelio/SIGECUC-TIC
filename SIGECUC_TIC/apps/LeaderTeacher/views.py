from django.template import RequestContext
from django.shortcuts import render_to_response


from apps.cursos.forms import Informacion_personalForm
from apps.cursos.models import LeaderTeacher
from apps.cursos.models import Cursos_Inscrito
from apps.cursos.models import Calificacion


from logica.leader_teacher_mediator import LeaderTeacherMediator

#=========================> Inicio pagina_leader_teacher_informacion_personal #=========================>
def pagina_leader_teacher_informacion_personal(request):
	
	leader_teacher_mediator = LeaderTeacherMediator()
	if request.method == "POST":
		#Opcion 2 para actualizar la informacion personal
		return leader_teacher_mediator.informacion_personal_task(request,2)
	else:
		#Opcion 1 para mostrar la informacion personal
		return leader_teacher_mediator.informacion_personal_task(request,1)
	
	
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
	curso_inscrito = Cursos_Inscrito.objects.filter(inscrito_id=id_leader_teacher)
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
