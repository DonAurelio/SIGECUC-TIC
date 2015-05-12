from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# URLS INICIO DE DE SESION  
	url(r'^master_teacher_informacion_personal', 'apps.MasterTeacher.views.pagina_master_teacher_informacion_personal', 
		name='master_teacher_informacion_personal'),
	
	

	

)