from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.contrib.auth.models import User
from apps.cursos.models import MasterTeacher
from apps.cursos.models import Curso
from apps.cursos.models import Cursos_Inscrito
from apps.cursos.models import Cohorte
from apps.cursos.models import Persona
from apps.cursos.models import LeaderTeacher
from django.contrib.auth.models import User

from .forms import UserForm
from .forms import PersonaForm
from apps.cursos.forms import Informacion_personalForm
from .forms import LeaderTeacherForm
from .forms import RegistroUserForm

from .models import RegistroUser

from django.core.mail import EmailMultiAlternatives
import datetime 




def pagina_registro(request):
	return render_to_response('registro.html')

def pagina_registro_informacion_personal(request):
	
	user = request.user
	user_id = user.id
		
	registro_user = RegistroUser.objects.get(user_id=user_id)
	persona = registro_user.persona
	persona_form = Informacion_personalForm(request.POST,instance=persona)

	if request.method == "POST":
		persona_form = Informacion_personalForm(request.POST,instance=persona)
		if persona_form.is_valid():
			email = persona_form.cleaned_data["email"]
			persona.email = email
			telefono = persona_form.cleaned_data["telefono"]
			persona.telefono = telefono
			direccion = persona_form.cleaned_data["direccion"]
			persona.direccion = direccion
			persona.save()
			mensaje = "Su informacion personal ha sido modificada correctamente"
			return render_to_response('registro_informacion_personal.html',{'user':user,'mensaje':mensaje})
	else:
		persona_form = Informacion_personalForm(request.POST, instance= persona) 

		persona_form = Informacion_personalForm(initial = {'identificacion' : persona.identificacion, 
			'primer_nombre' : persona.primer_nombre, 'segundo_nombre' : persona.segundo_nombre,
			'primer_apellido': persona.primer_apellido, 'segundo_apellido' : persona.segundo_apellido,
			'email' : persona.email, 'telefono' : persona.telefono, 
			'direccion' : persona.direccion

			})
	contexto = {'user':user, 'persona_form' : persona_form}
	return render_to_response('registro_informacion_personal.html',contexto, context_instance= RequestContext(request))


def pagina_registro_cambiar_clave(request):
	return HttpResponse('en contruccion')

def pagina_registrar_master_teacher(request):

	if request.method == "POST":
		form_user = UserForm(request.POST)
		form_persona = PersonaForm(request.POST)

		if form_user.is_valid() and form_persona.is_valid():
			add_user = form_user.save(commit=False)#noguarda todavia los datos semantienen
			username = request.POST.get('username')
			password = request.POST.get('password')	
			user = User.objects.create_user(username=username, password=password)
			user.save()

			add_persona = form_persona.save(commit=False)#noguarda todavia los datos semantienen
			ide_persona = form_persona.instance.pk #trae el id deacuerdo al form
			add_persona.save()#Guardamos la informacion

			ide_user= User.objects.get(username=username)
			master_teacher= MasterTeacher(ide_user.id, ide_persona)
			master_teacher.save()
			mensaje = "Su inscripcion se ha realizado con exito" 
			user = request.user
			contexto = {'user':user, 'mensaje':mensaje}
			return render_to_response('registro_registrar_master_teacher.html', contexto)
		else:
			form_persona = PersonaForm(request.POST)	
	else:
		form_user = UserForm()
		form_persona = PersonaForm()
	user = request.user
	ctx = {'user':user ,'form_persona':form_persona, 'form_user': form_user}
	return render_to_response('registro_registrar_master_teacher.html', ctx, context_instance= RequestContext(request))

def pagina_seleccionar_curso_cohorte(request):
	cursos = Curso.objects.all()
	contexto = {'cursos':cursos}
	return render_to_response('registro_seleccionar_curso_cohorte.html',contexto,context_instance=RequestContext(request))


def enviar_email_confirmacion(email, nombre_curso):
	subject = 'Asunto'
	text_content = 'Mensaje...nLinea 2nLinea3'
	html_content = '<h2>Notificacion Confircacion curso</h2><p>Confirmacion al curso</p>'
	html_content += nombre_curso 
	html_content += '<p>Ha sido Aceptado al curso</p>'
	from_email = '"SIGECUC-TIC" <emisor.telnet.univalle@gmail.com>'
	to = email
	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def pagina_crear_cohorte_curso(request, curso_id):

	if request.method == "POST":
		#Obtenemos la fecha del dia actual que indica el inicio de la cohorte
		fecha = datetime.date.today()
		hoy = fecha.strftime("%Y-%m-%d") 

		#Pasamos la fecha de fin al formato deseado de fechas
		fecha_fin = request.POST.get('id_datepicker')
		#return HttpResponse(fecha_fin)
		fecha_fin = fecha_fin.split('/')
		fecha_final = str(fecha_fin[2]+'-'+fecha_fin[1]+'-'+fecha_fin[0])
		data_time_field = datetime.datetime.strptime(fecha_final, '%Y-%m-%d')



		#Obtenemos la informacion del master teacher que dictara la cohorte
		master_teacher_id = request.POST.get('id_master_teacher')

		#Creamos la nueva cohorte en la cual estaran los leader teacher
		cohorte = Cohorte(fecha_inicio=hoy,fecha_fin=data_time_field,curso_id=curso_id,master_teacher_id=master_teacher_id)
		cohorte.save()

		cursos_inscrito = Cursos_Inscrito.objects.filter(curso_id=curso_id,estado='Pendiente')
		for curso_inscrito in cursos_inscrito:
			inscrito_id = request.POST.get(''+curso_inscrito.inscrito.persona.identificacion)
			
			if(not inscrito_id is None):
				username = curso_inscrito.inscrito.persona.identificacion
				password = curso_inscrito.inscrito.persona.primer_nombre +'-'+ str(curso_inscrito.inscrito.persona.identificacion)
				
				user = User.objects.create_user(username=username, password=password)
				user.save()

				#Asignamos el leader teacher a la cohorte 
				leader_teacher = LeaderTeacher(user_id=user.id,inscrito_id=curso_inscrito.inscrito.persona.identificacion)
				leader_teacher.save()
				leader_teacher.cohorte.add(cohorte)

				#Cambiamos el estado para el curso del inscrito 
				curso_inscrito.estado = 'Aceptado'
				curso_inscrito.save()
				
				#Enviamos un correo para indicar al inscrito que fue aceptado
				email = curso_inscrito.inscrito.persona.email
				enviar_email_confirmacion(email, curso_inscrito.curso.nombre)

		mensaje = "Se ha creado con exito una nueva cohorte para el curso " + cohorte.curso.nombre
		contexto = {'mensaje':mensaje}
		return render_to_response("registro_crear_cohorte.html",contexto,context_instance=RequestContext(request))


	else:
		inscritos_curso = Cursos_Inscrito.objects.filter(curso_id=curso_id,estado='Pendiente')
		curso = Curso.objects.get(id=curso_id)
		master_teachers = MasterTeacher.objects.all()
		contexto = {
		'curso':curso,
		'master_teachers':master_teachers,
		'inscritos':inscritos_curso}
		return render_to_response("registro_crear_cohorte.html",contexto,context_instance=RequestContext(request))