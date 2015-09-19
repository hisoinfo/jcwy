# -*- encoding: utf-8 -*-
from django.db import models


# Create your models here.
class CoinBalance(models.Model):
    """
    积分累计表
    """
    balance = models.IntegerField(default=0, help_text = '累计积分')
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    is_vip = models.BooleanField(help_text = '是否是vip')
    vip_effective_from = models.DateTimeField(null=True, blank=True, help_text = 'vip开始时间')
    vip_effective_to = models.DateTimeField(null=True, blank=True, help_text = 'vip结束时间')