from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.home', name='home'),
    url(r'^login/$', 'principal.views.login', name='login'),
    url(r'^servicios/$', 'principal.views.servicios', name='servicios'),
    url(r'^cerrar-sesion/$', 'principal.views.logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^plataformaCP/', include('plataformaCP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)