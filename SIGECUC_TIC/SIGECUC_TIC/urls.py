from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	#URLS DEL PROGRAMA GENERAL	
	
	url(r'^admin', include( admin.site.urls )),
	url(r'', include('apps.inicio.url', namespace='inicio')),
	url(r'', include('apps.inscripcion.url', namespace='inscripcion')),

)
