from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

from forms import LoginForm
from forms import InscripcionPersonaForm
from forms import HistorialLaboralForm
from forms import HistorialAcademicoForm
from .models import Curso
from .models import Inscrito

import datetime

from django.http import HttpResponse

# Create your views here.

def pagina_principal(request):
	#funcion que lista los cursos activos cuando el estado es 1
	cursos = Curso.objects.filter(estado='1')
	user = request.user
	context = { 'cursos':cursos,'user':user}
	return render_to_response('inicio.html',context)

def pagina_iniciar_sesion(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				if user.is_active:
					login(request,user)
					form = LoginForm()
					message = "Te has identificacdo de modo correcto"
					return render_to_response('master_teacher.html',{'user':user})
				else: 
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
		else:
			message = "Formulario no valido" 
	else:
		form = LoginForm()

	return render_to_response('login.html',{'message':message,'form':form}, context_instance=RequestContext(request))
	
def pagina_cerrar_sesion(request):
	user = request.user
	return render_to_response('inicio.html',{'user':user})


def pagina_informacion(request):
	user = request.user
	return render_to_response('informacion.html',{'user':user})



#==============================================================================
def listar_cursos(request):
    #funcion que lista los cursos activos cuando el estado es 1
	cursos = Curso.objects.filter(estado='1')
	return render(request, 'listar_cursos.html', { 'cursos': cursos })


def pagina_inscripcion_curso(request):
    id_course = request.GET.get('id_course')
    name_course = request.GET.get('name_course')
    #return render(request, 'inscripcion.html', {'id_course': id_course, 'name_course': name_course})
    return render_to_response('inscripcion_base.html')
    #html = "<html><body><h1>id course:</h1><h3>%s<h/3> <h1> Name curso</h1><h2>%s<h/2></body></html>" % (id_course, name_course)
    #return HttpResponse(html)


def inscripcion(request):
    return render_to_response('inscripcion.html')


def registre(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('identificacion', ''):
            errors.append('Por favor introduce la identificacion.')
        if not errors:
            values = [request.POST['identificacion'], request.POST['date_birth'],request.POST['sexo'],request.POST['caracter']]
            html = "<html><body><h1></h1><h3>conas %s</h3> </body></html>" % values[0]
            return HttpResponse(html)
    return render(request, 'inscripcion.html', {'errors': errors,'identificacion': request.POST.get('identificacion', ''),})


def pagina_inscripcion_persona(request):
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





