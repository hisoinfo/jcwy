# -*- coding:utf-8 -*-
from django.contrib.auth.models import User, Group
from .models import AdArea, Cigar, Adment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import list_route, detail_route 
from quickstart.serializers import UserSerializer, GroupSerializer, AdAreaSerializer, CigarSerializer, AdmentSerializer
from common.api import APIResponse
from rest_framework.response import Response


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    # queryset = AdArea.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)
    # queryset = User.objects.all()
    def get_queryset(self):
        user = self.request.user
        symbolfollows = SymbolFollow.objects.filter(user=user)
        return symbolfollows
    
    @list_route()
    def ads(self, request):
      '''
      查看用户信息
      '''
      users = User.objects.all()
      print users

      adarea = AdArea.objects.all()
      print adarea
      serializer = AdAreaSerializer(adarea, many=True)
      print serializer.data

      return APIResponse(serializer.data)

    
class GroupViewSet(viewsets.GenericViewSet):
    """
    允许查看和编辑group的 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    @list_route()
    def groups(self, request):
      return APIResponse("查看分组信息情况！")


class CigarViewSet(viewsets.GenericViewSet):

    """ Cigar resource. """
    
    serializer_class = CigarSerializer
    model = Cigar
    queryset = Cigar.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Return a list of objects.

        """
        return super(CigarViewSet, self).list(request, *args, **kwargs)

    @list_route()
    def set_price(self, request):
        """An example action to on the ViewSet."""
        return Response('20$')

    @list_route()
    def get_price(self, request):
        """Return the price of a cigar."""
        return Response('20$')


class AdAreaViewSet(viewsets.GenericViewSet):

    """ Cigar resource. """
    
    serializer_class = AdmentSerializer
    model = Adment
    # queryset = Adment.objects.all()

    def list(self, request, *args, **kwargs):
        """
        Return a list of objects.

        """
        return super(CigarViewSet, self).list(request, *args, **kwargs)

    @list_route()
    def set_price(self, request):
        """An example action to on the ViewSet."""
        return Response('20$')

    @list_route()
    def get_price(self, request):
        """Return the price of a cigar."""
        return APIResponse("serializer.data")

