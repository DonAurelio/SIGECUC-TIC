from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from aplicacion_cursos_tic.views import login
from aplicacion_cursos_tic.views import index
from aplicacion_cursos_tic.views import listar_cursos
from aplicacion_cursos_tic.views import send_course
from aplicacion_cursos_tic.views import inscripcion
from aplicacion_cursos_tic.views import registre
=======
from aplicacion_cursos_tic.views import login_page_view
from aplicacion_cursos_tic.views import index_page_view
from aplicacion_cursos_tic.views import contactenos_page_view
from aplicacion_cursos_tic.views import quienes_somos_page_view
>>>>>>> 90e1ddf447dc5333ee9ee09b9233c87c8eebb01a



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^login', login),
    url(r'^index', index),
    url(r'^listar_cursos', listar_cursos),
    url(r'^course/$', send_course),
    url(r'^inscripcion/$', inscripcion),
    url(r'^registre/$', registre)

=======
    url(r'^login/',login_page_view),
    url(r'^index/', index_page_view),
    url(r'^contactenos/',contactenos_page_view),
    url(r'^quienes_somos/',quienes_somos_page_view)
   
   
>>>>>>> 90e1ddf447dc5333ee9ee09b9233c87c8eebb01a
)
