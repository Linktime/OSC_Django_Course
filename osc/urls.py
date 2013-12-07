from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','views.index'),
    url(r'^tpl/$','views.diy_tpl'),
    url(r'^load_tpl/$','views.load_tpl'),
    url(r'^simple_tpl/$','views.simple_tpl'),
    # Examples:
    # url(r'^$', 'osc.views.home', name='home'),
    # url(r'^osc/', include('osc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
