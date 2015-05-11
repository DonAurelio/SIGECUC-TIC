from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse

from .forms import InscripcionPersonaForm
from .forms import HistorialLaboralForm
from .forms import HistorialAcademicoForm
from apps.cursos.models import Inscrito
import datetime


# Create your views here.
	
def inscripcion(request):
	return render_to_response('inscripcion.html')


def pagina_inscripcion_curso(request):
	#funcion que crea el formulario de inscripcion
	info = "iniciado"
	id_course = request.GET.get('id_course')
	name_course = request.GET.get('name_course')
	if request.method == "POST":
		form_persona = InscripcionPersonaForm(request.POST)
		form_HistorialAcademico = HistorialAcademicoForm(request.POST) 
		form_HistorialLaboral = HistorialLaboralForm(request.POST)
		if form_persona.is_valid() and form_HistorialAcademico.is_valid() and form_HistorialLaboral.is_valid():
			add_persona = form_persona.save(commit=False)#noguarda todavia los datos semantienen
			add_HistorialAcademico = form_HistorialAcademico.save(commit=False)#n oguarda todavia los datos semantienen
			add_HistorialLaboral = form_HistorialLaboral.save(commit=False)#n oguarda todavia los datos semantienen
			add_persona.save()#Guardamos la informacion
			ide_persona = form_persona.instance.pk #trae el id deacuerdo al form
			add_HistorialAcademico.save()
			ide_historialAcademico = form_HistorialAcademico.instance.pk
			add_HistorialLaboral.save() 
			ide_historialLaboral = form_HistorialLaboral.instance.pk
			#add_HistorialAcademico.save() #Guardamos la informacion
			#add_HistorialLaboral.save() #Guardamos la informacion
			form_persona.save_m2m() #Guarda las relaciones de ManyToMany
			form_HistorialAcademico.save_m2m() #Guarda las relaciones de ManyToMany
			form_HistorialLaboral.save_m2m() #Guarda las relaciones de ManyToMany
			fecha_actual =  datetime.datetime.now()

			inscrip= Inscrito(ide_persona, fecha_actual, True, ide_historialLaboral,ide_historialAcademico,id_course)
			inscrip.save()

			html = "<html><body><h1></h1><h3>Guardado %s</h3> </body></html>"
			return HttpResponse(html)
				
	else:
		form_persona = InscripcionPersonaForm()
		form_HistorialAcademico = HistorialAcademicoForm(request.POST) 
		form_HistorialLaboral = HistorialLaboralForm(request.POST)

	ctx = {'form_persona':form_persona, 'form_HistorialLaboral': form_HistorialLaboral, 'form_HistorialAcademico': form_HistorialAcademico,
	 'informacion':info, 'id_course':id_course, 'name_course':name_course}
	return render_to_response('inscripcion.html', ctx, context_instance= RequestContext(request))