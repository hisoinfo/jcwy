from django.conf.urls import patterns, include, url

from hisoinfo import api_rest
from hiso.router import router

router.register(r'coins', api_rest.CoinViewSet, 'coins') 


urlpatterns = patterns('')
