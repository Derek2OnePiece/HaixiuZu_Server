from django.conf.urls.defaults import patterns

urlpatterns = patterns('BasicServer.src.views.topic_views',
    (r'^pub_topic$', 'pub_topic_action'),
    (r'^update_topic$', 'update_topic_action'),
    (r'^get_topic_detail$', 'get_topic_detail_action'),
    
)
