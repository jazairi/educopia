from django.contrib import admin
admin.autodiscover()

from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lockssview.views.home', name='home'),
    url(r'^caches$', 'lockssview.views.caches.index'),
    url(r'^caches/(?P<obj_id>\d+)/$', 'lockssview.views.caches.detail'),
    url(r'^networks/(?P<network>\w+)/$', 'lockssview.views.caches.network'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
