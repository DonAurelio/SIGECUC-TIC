from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives

from .forms import InscripcionPersonaForm
from .forms import HistorialLaboralForm
from .forms import HistorialAcademicoForm
from .forms import InscripcionConsultaForm
from apps.cursos.models import Inscrito
import datetime

from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
	
def inscripcion(request):
	return render_to_response('inscripcion.html')

def enviar_email(email, nombre_curso):
	subject = 'Asunto'
	text_content = 'Mensaje...nLinea 2nLinea3'
	html_content = '<h2>Notificacion registro</h2><p>La inscripcion al curso</p>'
	html_content += nombre_curso 
	html_content += '<p>se ha realizado con exito, se informara a traves de este medio su aprobacion</p>'
	from_email = '"SIGECUC-TIC" <emisor.telnet.univalle@gmail.com>'
	to = email
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def pagina_incripcion_consulta(request):
	id_course = request.GET.get('id_course')
	name_course = request.GET.get('name_course')
	if request.method == "POST":
		form = InscripcionConsultaForm(request.POST)
		if form.is_valid():
			identificacion = request.POST.get('identificacion')
			
			try:
				inscrito = Inscrito.objects.get(persona_id=identificacion)
				return HttpResponse("Existe")
				fecha_actual =  datetime.datetime.now()
				inscrip= Inscrito(ide_persona, fecha_actual, True, ide_historialLaboral,ide_historialAcademico,id_curso)
				inscrip.save()
			except ObjectDoesNotExist:
				form_persona = InscripcionPersonaForm()
				form_HistorialAcademico = HistorialAcademicoForm() 
				form_HistorialLaboral = HistorialLaboralForm()

				ctx = {'form_persona':form_persona, 'form_HistorialLaboral': form_HistorialLaboral,'form_HistorialAcademico': form_HistorialAcademico,
				 'id_course':id_course, 'name_course':name_course}
				return render_to_response('inscripcion.html', ctx, context_instance= RequestContext(request))
	else:
		form = InscripcionConsultaForm()
	contexto = {'form':form}
	return render_to_response('inscripcion_consulta.html',contexto,context_instance= RequestContext(request))

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
			form_persona.save_m2m() #Guarda las relaciones de ManyToMany
			form_HistorialAcademico.save_m2m() #Guarda las relaciones de ManyToMany
			form_HistorialLaboral.save_m2m() #Guarda las relaciones de ManyToMany
			fecha_actual =  datetime.datetime.now()

			inscrip= Inscrito(ide_persona, fecha_actual, True, ide_historialLaboral,ide_historialAcademico,id_course)
			inscrip.save()
			email = request.POST.get('email')
			enviar_email(email, name_course)
			mensaje = "Su inscripcion se ha realizado con exito, se ha enviado una notificacion al correo %s" %email 
			contexto = {'mensaje':mensaje}
			return render_to_response('inscripcion.html',contexto)
		else:
			form_persona = InscripcionPersonaForm(request.POST)
			form_HistorialAcademico = HistorialAcademicoForm(request.POST) 
			form_HistorialLaboral = HistorialLaboralForm(request.POST)
		
	else:
		form_persona = InscripcionPersonaForm()
		form_HistorialAcademico = HistorialAcademicoForm() 
		form_HistorialLaboral = HistorialLaboralForm()

	ctx = {'form_persona':form_persona, 'form_HistorialLaboral': form_HistorialLaboral,'form_HistorialAcademico': form_HistorialAcademico,
	 'informacion':info, 'id_course':id_course, 'name_course':name_course}
	return render_to_response('inscripcion.html', ctx, context_instance= RequestContext(request))