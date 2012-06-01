from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='home'),
    url(r'^guestbook/add', 'main.views.agregar', name="agregar"),
    url(r'^guestbook/(?P<id>\d+)/edit', 'main.views.editar', name="editar"),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
