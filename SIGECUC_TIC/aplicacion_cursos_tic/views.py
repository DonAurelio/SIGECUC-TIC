from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

from forms import LoginForm
from forms import addInscripcionForm
from .models import Curso

from django.http import HttpResponse

# Create your views here.

def pagina_principal(request):
	#funcion que lista los cursos activos cuando el estado es 1
	cursos = Curso.objects.filter(estado='1')
	context = { 'cursos':cursos }
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
					
					message = "Te has identificacdo de modo correcto"
				else: 
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = LoginForm()

	return render_to_response('login.html',{'message':message,'form':form}, context_instance=RequestContext(request))
	

def pagina_informacion(request):
	return render_to_response('informacion.html')



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


def add_inscripcion_view(request):
    info = "iniciado"
    if request.method == "POST":
        form = addInscripcionForm(request.POST)
    else:
        form = addInscripcionForm()
    ctx = {'form':form, 'informacion':info}
    return render_to_response('add_inscripcion.html', ctx, context_instance= RequestContext(request))





