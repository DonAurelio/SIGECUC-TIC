from django.conf.urls import patterns, include, url
from django.contrib import admin
<<<<<<< HEAD
from aplicacion_cursos_tic.views import login
from aplicacion_cursos_tic.views import index
from aplicacion_cursos_tic.views import listar_cursos
from aplicacion_cursos_tic.views import send_course
from aplicacion_cursos_tic.views import inscripcion
from aplicacion_cursos_tic.views import registre
from aplicacion_cursos_tic.views import add_inscripcion_view
from aplicacion_cursos_tic.views import contact

=======
>>>>>>> 09b5ecde95aa6b77dc821a97611f0d2677750d77

from aplicacion_cursos_tic.views import index_page_view
from aplicacion_cursos_tic.views import login_page_view
from aplicacion_cursos_tic.views import contact_page_view
from aplicacion_cursos_tic.views import information_page_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

<<<<<<< HEAD
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
=======
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^index', index_page_view, name='index'),
    url(r'^login.html', login_page_view, name='login'),
    url(r'^contact$', contact_page_view, name='contact'),
    url(r'^information$', information_page_view, name='information'),

      
    )
>>>>>>> 09b5ecde95aa6b77dc821a97611f0d2677750d77
