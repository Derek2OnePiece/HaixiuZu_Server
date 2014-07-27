from django.conf.urls.defaults import patterns

urlpatterns = patterns('BasicServer.src.views.user_views',
    (r'^login$', 'login_action'),
    (r'^logout$', 'logout_action'),

)
