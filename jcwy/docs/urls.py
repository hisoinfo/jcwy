from django.conf.urls import patterns
from django.conf.urls import url
#from rest_framework_swagger.views import SwaggerResourcesView, SwaggerApiView, SwaggerUIView
from rest_framework_swagger.views import SwaggerResourcesView, SwaggerUIView
from .views import DocsApiView

urlpatterns = patterns('',
    url(r'^$', SwaggerUIView.as_view(), name="django.swagger.base.view"),
    url(r'^api-docs/$', SwaggerResourcesView.as_view(), name="django.swagger.resources.view"),
    url(r'^api-docs/(?P<path>.*)/?$', DocsApiView.as_view(), name='django.swagger.api.view'),
)
