# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework import routers
from quickstart import views
from django.contrib import admin
admin.autodiscover()


router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)	


urlpatterns = [
    # Examples:
    url(r'^home/$', 'property.views.home', name='home'),
    url(r'^index/$', 'property.views.index', name='index'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^', include(router.urls)),
    url(r'^api/v1/', include('jcwy.api_urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
