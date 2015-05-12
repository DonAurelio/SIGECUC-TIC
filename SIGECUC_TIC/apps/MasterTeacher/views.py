from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import Persona_MasterTeacherForm
from apps.cursos.models import MasterTeacher
import hashlib


# Create your views here.

def pagina_master_teacher_informacion_personal(request):
	user = request.user
	user_id = user.id
	#consulta a Mater Teacher
	master_teacher = MasterTeacher.objects.get(user_id=user_id)
	if request.method == "POST":
		#se instancia el master_teacher para que pase la validez y sea un formulario para modificar
		form_personaMasterTeacher = Persona_MasterTeacherForm(request.POST, instance=master_teacher)
		if form_personaMasterTeacher.is_valid():
			email = form_personaMasterTeacher.cleaned_data["email"]
			master_teacher.persona.email = email
			telefono = form_personaMasterTeacher.cleaned_data["telefono"]
			master_teacher.persona.telefono = telefono
			direccion = form_personaMasterTeacher.cleaned_data["direccion"]
			master_teacher.persona.direccion = direccion
			master_teacher.persona.save()
			mensaje = "Su informacion personal ha sido modificada correctamente"
			return render_to_response('master_teacher.html',{'user':user,'mensaje':mensaje})
	
	else:
		form_personaMasterTeacher = Persona_MasterTeacherForm(request.POST, instance= master_teacher) 

		form_personaMasterTeacher = Persona_MasterTeacherForm(initial = {'identificacion' : master_teacher.persona.identificacion, 
			'primer_nombre' : master_teacher.persona.primer_nombre, 'segundo_nombre' : master_teacher.persona.segundo_nombre,
			'primer_apellido': master_teacher.persona.primer_apellido, 'segundo_apellido' : master_teacher.persona.segundo_apellido,
			'email' : master_teacher.persona.email, 'telefono' : master_teacher.persona.telefono, 
			'direccion' : master_teacher.persona.direccion

			})
	contexto = {'user':user, 'form_personaMasterTeacher' : form_personaMasterTeacher}
	return render_to_response('master_teacher_informacion_personal.html',contexto, context_instance= RequestContext(request))


