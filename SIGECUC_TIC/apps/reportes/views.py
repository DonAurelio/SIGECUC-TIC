from django.shortcuts import render, render_to_response

# Create your views here.

def principal(request):
	user = request.user
	mensaje = " bienvenid@ al modulo de reportes,"
	mensaje += " por favor seleccione el reporte que "
	mensaje += "desea visualzar."
		
	contexto = {'user':user, 'mensaje':mensaje}
	return render_to_response('principal.html',contexto)
	
def reporte_notas_por_estudiantes(request):
	user = request.user
	contexto = {'user':user}
	return render_to_response('tabla1.html',contexto)
