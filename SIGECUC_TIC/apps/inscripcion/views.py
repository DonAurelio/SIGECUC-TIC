from django.shortcuts import render

# Create your views here.
def pagina_inscripcion_curso(request):
	id_course = request.GET.get('id_course')
	name_course = request.GET.get('name_course')
	return render_to_response('inscripcion_base.html')