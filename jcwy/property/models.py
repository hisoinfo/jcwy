# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Members(models.Model):
    member_id = models.IntegerField(null=False, help_text='用户ID')
    member_name = models.CharField(null=False, max_length=20, help_text='用户姓名')
    pwd = models.CharField(null=False, max_length=20, help_text='用户密码')
    regist_date = models.DateTimeField(auto_now_add=True)
    
    #返回用户名S
    def __unicode__(self):
    	return self.member_name
