
from django.conf.urls import patterns, include, url
from router import router, router_no_slash

urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^quickstart/', include('quickstart.api_urls')),
    # url(r'^coins/', include('coins.api_urls')),
    # url(r'^ads/', include('ads.api_urls')),
    # url(r'^shakes/', include('shakes.api_urls')),
)

urlpatterns += patterns('',
    url(r'', include(router.urls)),
    url(r'', include(router_no_slash.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)