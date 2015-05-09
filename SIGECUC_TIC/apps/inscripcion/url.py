from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# URLS INICIO DE DE SESION  
	url(r'^inscripcion', 'apps.inscripcion.views.pagina_inscripcion_curso', name='inscripcion'),
	
	

	

)