from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# URLS INICIO DE DE SESION  
	
	#url(r'^principal',PaginaPrincipalDetailView.as_view(),name="principal"),
	#rl(r'^principal/(?P<slug>[-\w])/',PaginaPrincipalDetailView.as_view(),name="principal"),
	
	url(r'^$','apps.inicio.views.pagina_principal',name="principal"),
	url(r'^principal','apps.inicio.views.pagina_principal',name="principal"),
	url(r'^login','apps.inicio.views.pagina_iniciar_sesion',name="login"),
	url(r'^perfil','apps.inicio.views.pagina_perfil',name="perfil"),
	url(r'^cerrarsesion','django.contrib.auth.views.logout',{'next_page':'/'}, name="cerrarsesion"),
	url(r'^informacion','apps.inicio.views.pagina_informacion',name="informacion"),
	

	

)