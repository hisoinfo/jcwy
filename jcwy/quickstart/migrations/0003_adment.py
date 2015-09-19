# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20150919_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'ads Name', max_length=25)),
                ('position', models.CharField(default=b'locate', max_length=30)),
                ('notes', models.TextField()),
            ],
        ),
    ]
