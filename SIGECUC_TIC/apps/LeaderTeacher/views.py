from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User

#from .forms import Persona_MasterTeacherForm
from apps.cursos.forms import Informacion_personalForm
from apps.cursos.models import LeaderTeacher

# Create your views here.

def pagina_leader_teacher_informacion_personal(request):
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
