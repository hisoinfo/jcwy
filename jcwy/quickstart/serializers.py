# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, Group
from .models import AdArea, Cigar, Adment
from rest_framework import serializers, fields




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CigarSerializer(serializers.ModelSerializer):
    url = fields.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Cigar

class AdAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdArea
        fields = ('id','code', 'title', 'description')

class AdmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adment