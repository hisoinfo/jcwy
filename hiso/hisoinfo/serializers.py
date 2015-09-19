# -*- encoding: utf-8 -*-

from django.db import models

from rest_framework import serializers
from .models import CoinBalance


class CoinBalanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoinBalance
       