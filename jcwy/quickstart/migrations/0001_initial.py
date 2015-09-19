# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(help_text=b'\xe5\xb9\xbf\xe5\x91\x8a\xe4\xbd\x8d\xe4\xbb\xa3\xe7\xa0\x81', unique=True, max_length=20)),
                ('title', models.CharField(help_text=b'\xe5\xb9\xbf\xe5\x91\x8a\xe4\xbd\x8d\xe6\xa0\x87\xe9\xa2\x98', max_length=100)),
                ('description', models.CharField(help_text=b'\xe5\xb9\xbf\xe5\x91\x8a\xe4\xbd\x8d\xe6\x8f\x8f\xe8\xbf\xb0', max_length=200)),
                ('status', models.IntegerField(default=0, help_text=b'\xe8\xae\xb0\xe5\xbd\x95\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe6\x9c\x89\xe6\x95\x88'), (0, b'\xe6\x97\xa0\xe6\x95\x88')])),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
