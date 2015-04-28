from django.conf.urls import patterns, include, url
from django.contrib import admin

from aplicacion_cursos_tic.views import index_page_view
from aplicacion_cursos_tic.views import login_page_view
from aplicacion_cursos_tic.views import contact_page_view
from aplicacion_cursos_tic.views import information_page_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/$', include(admin.site.urls)),
    url(r'^index', index_page_view, name='index'),
    url(r'^login.html', login_page_view, name='login'),
    url(r'^contact$', contact_page_view, name='contact'),
    url(r'^information$', information_page_view, name='information'),

      
    )
