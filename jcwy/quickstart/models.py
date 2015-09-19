# -*- encoding: utf-8 -*-
from django.db import models

STATUS_TYPE_CHOICES = (
        (1, '有效'),
        (0, '无效'),
        )

class AdArea(models.Model):
    code = models.CharField(max_length=20, unique=True, help_text='代码')
    title = models.CharField(max_length=100, help_text='标题')
    description = models.CharField(max_length=200, help_text='描述')
    status = models.IntegerField(default=0, choices=STATUS_TYPE_CHOICES, help_text='状态') # 1-有效 0-无效 
    modified_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Cigar(models.Model):
    FORM_CHOICES = (
        ('parejo', 'Parejo'),
        ('torpedo', 'Torpedo'),
        ('pyramid', 'Pyramid'),
        ('perfecto', 'Perfecto'),
        ('presidente', 'Presidente'),
    )
    name = models.CharField(max_length=25, help_text='Cigar Name')
    colour = models.CharField(max_length=30, default="Brown")
    form = models.CharField(max_length=20, choices=FORM_CHOICES, default='parejo')
    gauge = models.IntegerField()
    length = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=5)
    notes = models.TextField()

    def get_absolute_url(self):
        return "/api/cigars/%i/" % self.id

class Adment(models.Model):
    name = models.CharField(max_length=25, help_text='ads Name')
    position = models.CharField(max_length=30, default="locate")
    notes = models.TextField()
