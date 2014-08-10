from django.conf.urls.defaults import patterns

urlpatterns = patterns('BasicServer.src.views.user_views',
    (r'^login$', 'login_action'),
    (r'^third_party_login$', 'third_party_login_action'),
    (r'^logout$', 'logout_action'),
    (r'^register$', 'register_action'),
    (r'^get_user_profile$', 'get_user_profile_action'),
    (r'^update_user_profile$', 'update_user_profile_action'),

)
