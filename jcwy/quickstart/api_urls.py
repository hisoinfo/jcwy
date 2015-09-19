# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, include, url

from quickstart import api_rest, views
from jcwy.router import router

# router.register(r'qs/test', api_rest.TestViewSet, 'ads') 
# router.register(r'quickstart/users', views.UserViewSet, 'ads') 
router.register(r'account/groups', api_rest.GroupViewSet, 'ads') 
router.register(r'account/users', api_rest.UserViewSet, 'ads') 
router.register(r'test/api_test', api_rest.AdAreaViewSet, 'ads') 
router.register(r'cigar/test', api_rest.CigarViewSet, 'ads') 


urlpatterns = patterns('')