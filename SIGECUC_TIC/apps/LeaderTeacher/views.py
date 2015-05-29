from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from apps.cursos.forms import Informacion_personalForm
from apps.cursos.models import LeaderTeacher
from apps.cursos.models import Cursos_Inscrito
from apps.cursos.models import Calificacion


from logica.leader_teacher_mediator import LeaderTeacherMediator

def pagina_leader_teacher_informacion_personal(request):
	
	leader_teacher_mediator = LeaderTeacherMediator()
	if request.method == "POST":
		#Opcion 2 para actualizar la informacion personal
		return leader_teacher_mediator.informacion_personal_task(request,2)
	else:
		#Opcion 1 para mostrar la informacion personal
		return leader_teacher_mediator.informacion_personal_task(request,1)
	
def pagina_consulta_cursos_calificados(request):
	leader_teacher_mediator = LeaderTeacherMediator()
	return leader_teacher_mediator.calificaciones_task(request=request,option=1)

def pagina_leader_teacher_descripcion_calificacion(request,cohorte_id):
	leader_teacher_mediator = LeaderTeacherMediator()
	return leader_teacher_mediator.calificaciones_task(request=request,cohorte_id=cohorte_id,option=2)

def pagina_generar_certificado(request):
	return render_to_response('certificado.html',context_instance=RequestContext(request))



