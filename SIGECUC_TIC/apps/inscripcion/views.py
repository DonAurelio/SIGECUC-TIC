from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .forms import InscripcionPersonaForm
from .forms import HistorialLaboralForm
from .forms import HistorialAcademicoForm
from .forms import InscripcionConsultaForm

from apps.cursos.models import Inscrito
from apps.cursos.models import Cursos_Inscrito

from logica.utilidad import TraductorFecha

import datetime

from logica.inscription_builder import InscriptionDirector
# Create your views here.
	
def inscripcion(request):
	return render_to_response('inscripcion.html')



def pagina_incripcion_consulta(request):
	id_course = request.GET.get('id_course')
	name_course = request.GET.get('name_course')
	if request.method == "POST":
		form = InscripcionConsultaForm(request.POST)
		if form.is_valid():

			identificacion = request.POST.get('identificacion')
			
			try:
				inscrito = Inscrito.objects.get(persona_id=identificacion)
				
				fecha_actual =  datetime.datetime.now()
				
				curso_inscrito = Cursos_Inscrito(curso_id=id_course, inscrito_id=identificacion, fecha_inscripcion=fecha_actual, estado='Pendiente')
				curso_inscrito.save()

				email = inscrito.persona.email
				mensaje = "Su inscripcion se ha realizado con exito, se ha enviado una notificacion al correo %s" %email 
				contexto = {'mensaje':mensaje}
				return render_to_response('inscripcion.html',contexto)

			except ObjectDoesNotExist:
				
				return pagina_inscripcion_curso(request)
	else:
		form = InscripcionConsultaForm()
	contexto = {'form':form}
	return render_to_response('inscripcion_consulta.html',contexto,context_instance= RequestContext(request))

def pagina_inscripcion_curso(request):

	director_inscripction = InscriptionDirector()
	return director_inscripction.construct(request)


	