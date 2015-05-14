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
	url(r'', include('apps.MasterTeacher.url', namespace = 'masterTeacher')),
	url(r'', include('apps.LeaderTeacher.url', namespace= 'leaderTeacher')),

		# Change Password URLs:
	url(r'^accounts/password_change/$', 
		'django.contrib.auth.views.password_change', 
		{'post_change_redirect' : '/accounts/password_change/done/'}, 
		name="password_change"),
		(r'^accounts/password_change/done/$', 
		'django.contrib.auth.views.password_change_done'),

)
