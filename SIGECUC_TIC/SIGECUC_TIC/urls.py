from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^admin/', include( admin.site.urls ), name='admin'), 
    url(r'^$', 'aplicacion_cursos_tic.views.index_page_view', name='index'),
    url(r'^index', 'aplicacion_cursos_tic.views.index_page_view', name='index'),
    url(r'^login', 'aplicacion_cursos_tic.views.login_page_view', name='login'),
    url(r'^contact', 'aplicacion_cursos_tic.views.contact_page_view', name='contact'),
    url(r'^information', 'aplicacion_cursos_tic.views.information_page_view', name='information')
    #url(r'^login', login),
    #url(r'^index', index),
    #url(r'^contactenos', contact),
    #url(r'^listar_cursos', listar_cursos),
    #url(r'^course/$', send_course),
    #url(r'^inscripcion/$', inscripcion),
    #url(r'^registre/$', registre),
    #url(r'add_inscripcion/$', add_inscripcion_view)

)
