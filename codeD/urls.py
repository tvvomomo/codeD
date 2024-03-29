from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'codeD.views.home', name='home'),
    # url(r'^codeD/', include('codeD.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'brainstorm.views.index'),
    url(r'^word/(\d+)/$', 'brainstorm.views.showWord'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
