from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from apps.cursos.forms import Informacion_personalForm
from apps.cursos.models import LeaderTeacher
from apps.cursos.models import Cursos_Inscrito
from apps.cursos.models import Calificacion, Cohorte, Calificacion

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from logica.leader_teacher_mediator import LeaderTeacherMediator

from easy_pdf.rendering import render_to_pdf_response

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


def calcular_nota_final_curso(calificaciones):
		nota_final = 0.0
		#funcion que calcula la nota final del curso con su peso en porcentaje
		for calificacion in calificaciones:
			nota_parcial = float(calificacion.nota_actividad)
			porcentaje_actividad = float(calificacion.actividad.peso)
			nota_final = nota_final + (nota_parcial * porcentaje_actividad)
		return nota_final


def pagina_generar_certificado(request , cohorte_id):
	user = request.user
	user_id = user.id
	#id_cohorte = request.GET.get('id_cohorte')
	

	cohorte = Cohorte.objects.get(id=cohorte_id)
	curso_id = cohorte.curso.id

	#Se busca la identificacion del Leader Teacher
	leader_teacher = LeaderTeacher.objects.get(user_id=user_id)
	id_leader_teacher = leader_teacher.inscrito.persona.identificacion

	#se busca el curso que pertenece el inscrito
	curso_inscrito = Cursos_Inscrito.objects.get(inscrito_id=id_leader_teacher,curso__id=curso_id)
	#Se busca las calificaciones ordenando por attividad
	calificaciones = Calificacion.objects.filter(leader_teacher_id=id_leader_teacher, cohorte_id=cohorte_id).order_by('actividad_id')
	#usa fiuncion para calcular la nota_final
	nota_final = calcular_nota_final_curso(calificaciones)

	mensaje = ""
	tipo_certificado = ""
	if nota_final == 3.0:
		mensaje = "Asistio al curso"
		tipo_certificado = "Certificado de Asistencia"
	elif nota_final >= 3.1 and nota_final <= 3.5:
		mensaje = "Participo en el curso"
		tipo_certificado = "Certificado de Participacion"
	else:
		mensaje = "Aprobo en el curso"
		tipo_certificado = "Certificado de Excelencia"

	contexto = {
	'tipo_certificado':tipo_certificado,
	'mensaje':mensaje,
	'leader_teacher':leader_teacher,
	'curso':curso_inscrito.curso.nombre}
	
	return render_to_response('certificado.html',contexto, context_instance=RequestContext(request))

def imprimir_certificado(request, cohorte_id):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawCentredString(0, 0, "Centro de Innovacion Educativa Regional de la Region Sur de Colombia")
    p.drawCentredString(100, 100, "Certificado de Asistencia")
    p.drawCentredString(100, 100, "Hace constar que")
    p.drawCentredString(100, 100, "Aurelio Antonio Vivas Meza")
    p.drawCentredString(100, 100, "identificado con la Cedula de Ciudadania")
    p.drawCentredString(100, 100, "1008989089089")
    p.drawCentredString(100, 100, "Asistio al Curso")
    p.drawCentredString(100, 100, "Matematicas Discretas II")
    p.drawCentredString(100, 100, "obteniendo un promedio de ")
    p.drawCentredString(100, 100, "3.5")
    

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response