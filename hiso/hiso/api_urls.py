
from django.conf.urls import patterns, include, url
from router import router, router_no_slash

urlpatterns = patterns('',

    url(r'^hisoinfo/', include('hisoinfo.api_urls')),

)

urlpatterns += patterns('',
    url(r'', include(router.urls)),
    url(r'', include(router_no_slash.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
