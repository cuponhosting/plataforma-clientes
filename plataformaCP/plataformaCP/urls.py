from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'principal.views.home', name='home'),
    url(r'^$', RedirectView.as_view(url='/servicios/')),
    url(r'^servicios/$', 'principal.views.servicios', name='servicios'),
    url(r'^cerrar-sesion/$', 'principal.views.cerrarsesion', name='cerrarsesion'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$', 'principal.views.login', name='login'),
    url(r'^login/$', login, {'template_name': 'login.html', }, name="login"),
    # url(r'^plataformaCP/', include('plataformaCP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)