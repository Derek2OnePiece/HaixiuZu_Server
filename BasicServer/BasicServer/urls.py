from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BasicServer.views.home', name='home'),
    # url(r'^BasicServer/', include('BasicServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
    url(r'^user/', include('BasicServer.src.urls.user_urls')),
    url(r'^topic/', include('BasicServer.src.urls.topic_urls')),
    url(r'^comment/', include('BasicServer.src.urls.comment_urls')),
)
