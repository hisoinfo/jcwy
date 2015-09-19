# -*- encoding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import status,mixins,parsers
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework import status
from .serializers import CoinBalanceSerializer
from .api import APIResponse

class CoinViewSet(viewsets.GenericViewSet):
    serializer_class = CoinBalanceSerializer

    @list_route()
    def balance(self, request, *args, **kwargs):
        '''
        获取用户累计积分信息
        ---------------------------------------------------

        成功返回示例:
        -------------
        :: 

            {
              "balance": 100 #累计积分 
            }

        错误返回:
        ---------

        =======================  =========================== 
              error_key                 response
        =======================  =========================== 
        =======================  ===========================    
        '''

        print 'test'

        return APIResponse("datat====")