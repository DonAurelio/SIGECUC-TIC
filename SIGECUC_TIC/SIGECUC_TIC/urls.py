from django.conf.urls import patterns, include, url
from django.contrib import admin
from aplicacion_cursos_tic.views import login_page_view
from aplicacion_cursos_tic.views import index_page_view
from aplicacion_cursos_tic.views import contactenos_page_view
from aplicacion_cursos_tic.views import quienes_somos_page_view



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login_page_view),
    url(r'^index/', index_page_view),
    url(r'^contactenos/',contactenos_page_view),
    url(r'^quienes_somos/',quienes_somos_page_view)
   
   
)
