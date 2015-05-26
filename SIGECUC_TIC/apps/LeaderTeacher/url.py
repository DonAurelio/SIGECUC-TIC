from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# URLS INICIO DE DE SESION  
	url(r'^leader_teacher_informacion_personal', 'apps.LeaderTeacher.views.pagina_leader_teacher_informacion_personal', 
		name='leader_teacher_informacion_personal'),
	#url(r'^leader_teacher_calificaciones', 'apps.LeaderTeacher.views.pagina_leader_teacher_calificaciones', 
	#	name='leader_teacher_calificaciones'),
	url(r'^leader_teacher_calificaciones', 'apps.LeaderTeacher.views.pagina_consulta_cursos_calificados', 
		name='leader_teacher_calificaciones'),
	url(r'^leader_teacher_descripcion_calificacion', 
		'apps.LeaderTeacher.views.pagina_leader_teacher_descripcion_calificacion',
	name='leader_teacher_descripcion_calificacion'),

	url(r"^clientes/(?P<cliente>[^/]+)/$", tuvista),
)