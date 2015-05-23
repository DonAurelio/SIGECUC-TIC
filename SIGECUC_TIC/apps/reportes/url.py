from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	#URLS DEL PROGRAMA GENERAL	
	url(r'^reportes', 'apps.reportes.views.principal', name='principal'),
	url(r'^notas_estudiantes', 'apps.reportes.views.reporte_notas_por_estudiantes', name='reporte1'),
	
)