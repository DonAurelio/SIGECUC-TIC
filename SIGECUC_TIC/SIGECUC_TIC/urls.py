from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	
	# URLS INICIO DE DE SESION  
	url(r'^$', 'aplicacion_cursos_tic.views.pagina_principal'),
	url(r'^admin', include( admin.site.urls )),
	url(r'^inicio', 'aplicacion_cursos_tic.views.pagina_principal'),
	url(r'^login', 'aplicacion_cursos_tic.views.pagina_iniciar_sesion'),
	url(r'^perfil', 'aplicacion_cursos_tic.views.pagina_perfil'),
	url(r'^cerrar_sesion','django.contrib.auth.views.logout',{'next_page':'/'}),
	url(r'^informacion', 'aplicacion_cursos_tic.views.pagina_informacion'),


	url(r'^inscripcion', 'aplicacion_cursos_tic.views.pagina_inscripcion_persona'),

	#URLS MASTER TEACHER
	url(r'^master_teacher_informacion_personal', 'aplicacion_cursos_tic.views.pagina_master_teacher_informacion_personal'),
	url(r'^master_teacher_actividades_evaluacion', 'aplicacion_cursos_tic.views.pagina_master_teacher_actividades_evaluacion'),
	url(r'^master_teacher_estudiantes', 'aplicacion_cursos_tic.views.pagina_master_teacher_estudiantes'),

	#URSL LEADER TEACHER
	url(r'^leader_teacher_informacion_personal', 'aplicacion_cursos_tic.views.pagina_leader_teacher_informacion_personal'),
	url(r'^leader_teacher_informacion_curso', 'aplicacion_cursos_tic.views.pagina_leader_teacher_informacion_curso'),
	url(r'^leader_teacher_calificaciones', 'aplicacion_cursos_tic.views.pagina_leader_teacher_calificaciones'),
	url(r'^leader_teacher_historial_academico', 'aplicacion_cursos_tic.views.pagina_leader_teacher_historial_academico'),
	url(r'^leader_teacher_certificados_obtenidos', 'aplicacion_cursos_tic.views.pagina_leader_teacher_certificados_obtenidos'),
	

	#url(r'^inscripcion', 'aplicacion_cursos_tic.views.enviar_curso',name='env_curso'),
	#url(r'^login', login),
	#url(r'^index', index),
	#url(r'^contactenos', contact),
	#url(r'^listar_cursos', listar_cursos),
	#url(r'^course/$', send_course),
	#url(r'^inscripcion/$', inscripcion),
	#url(r'^registre/$', registre),
	#url(r'add_inscripcion/$', add_inscripcion_view)

)
