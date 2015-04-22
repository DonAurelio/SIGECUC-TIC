from django.conf.urls import patterns, include, url
from django.contrib import admin
from aplicacion_cursos_tic.views import Login


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', aplicacion_cursos_tic.views.login),
   
)
