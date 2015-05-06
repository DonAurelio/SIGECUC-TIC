from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    # URLS INICIO DE DE SESION  
    url(r'^$', 'aplicacion_cursos_tic.views.pagina_principal', name='inicio'),
    url(r'^admin', include( admin.site.urls ), name='admin'),
    url(r'^inicio', 'aplicacion_cursos_tic.views.pagina_principal', name='inicio'),
    url(r'^login', 'aplicacion_cursos_tic.views.pagina_iniciar_sesion', name='sesion'),
    url(r'^perfil', 'aplicacion_cursos_tic.views.pagina_perfil',name='perfil'),
    url(r'^cerrar_sesion', 'django.contrib.auth.views.logout',{'next_page':'/'}),
    url(r'^informacion', 'aplicacion_cursos_tic.views.pagina_informacion', name='informacion'),


    url(r'^inscripcion', 'aplicacion_cursos_tic.views.pagina_inscripcion_persona',name='env_curso'),

    #URLS MASTER TEACHER
    url(r'^master_teacher/informacion_personal', 'aplicacion_cursos_tic.views.pagina_master_teacher_informacion_personal',name='informacion personal'),
    url(r'^master_teacher/actividades_evaluacion', 'aplicacion_cursos_tic.views.pagina_master_teacher_actividades_evaluacion',name='actividades evaluacion'),
    url(r'^master_teacher/estudiantes', 'aplicacion_cursos_tic.views.pagina_master_teacher_estudiantes',name='estudiantes'),
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
