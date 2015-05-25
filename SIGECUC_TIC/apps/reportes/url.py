from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'SIGECUC_TIC.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	#URLS DEL PROGRAMA GENERAL	
	url(r'^reportes', 'apps.reportes.views.principal', name='principal'),
	url(r'^notas_estudiantes', 'apps.reportes.views.reporte_notas_por_estudiantes', name='reporte1'),
	url(r'^cursos_aprobados', 'apps.reportes.views.reporte_estudiantes_cursos_aprobados', name='reporte2'),
	url(r'^estudiantes_curso_departamento', 'apps.reportes.views.reporte_estudiantes_curso_por_departamento', name='reporte3'),
	url(r'^cursos_numero_asitentes', 'apps.reportes.views.reporte_cursos_numero_asitentes', name='reporte4'),
	url(r'^docentes_estudiantes_departamento', 'apps.reportes.views.reporte_docentes_estudiantes_departamento', name='reporte5'),
	url(r'^cursos_menor_potencial_avance', 'apps.reportes.views.reporte_cursos_menor_potencial_avance', name='reporte6'),
	url(r'^reporte_porcentaje_estudiantes_aprobados_cursos_departamentos', 'apps.reportes.views.reporte_porcentaje_estudiantes_aprobados_cursos_departamentos', name='reporte7'),
	url(r'^reporte_porcentaje_estudiantes_reprobados_cursos_departamentos', 'apps.reportes.views.reporte_porcentaje_estudiantes_reprobados_cursos_departamentos', name='reporte8'),
	
	
)