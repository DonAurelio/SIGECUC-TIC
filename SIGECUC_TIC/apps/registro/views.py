from django.shortcuts import render, render_to_response

def pagina_registro(request):
	return render_to_response('registro.html')
