from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# URLS INICIO DE DE SESION  
	
	#url(r'^principal',PaginaPrincipalDetailView.as_view(),name="principal"),
	#url(r'^principal/(?P<slug>[-\w])/',PaginaPrincipalDetailView.as_view(),name="principal"),
	
	url(r'^$','apps.registro.views.pagina_registro',name="pagina_registro"),
	url(r'^registrar_master_teacher', 'apps.registro.views.pagina_registrar_master_teacher', 
		name='registrar_master_teacher'),

	
	
)