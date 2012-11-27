from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'main.views.index', name='home'),
	url(r'^guestbook/add', 'main.views.agregar', name='agregar'),
	url(r'^guestbook/edit/(?P<id>\d+)', 'main.views.editar', name='editar'),
	url(r'^guestbook/del/(?P<id>\d+)', 'main.views.eliminar', name='eliminar'),
)
