from django.conf.urls import patterns, include, url
from django.contrib import admin
from aplicacion_cursos_tic.views import login
from aplicacion_cursos_tic.views import index
from aplicacion_cursos_tic.views import listar_cursos
from aplicacion_cursos_tic.views import send_course
from aplicacion_cursos_tic.views import inscripcion
from aplicacion_cursos_tic.views import registre
from aplicacion_cursos_tic.views import add_inscripcion_view
from aplicacion_cursos_tic.views import contact



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', login),
    url(r'^index', index),
    url(r'^contactenos', contact),
    url(r'^listar_cursos', listar_cursos),
    url(r'^course/$', send_course),
    url(r'^inscripcion/$', inscripcion),
    url(r'^registre/$', registre),
    url(r'add_inscripcion/$', add_inscripcion_view)

)
