# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cigar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Cigar Name', max_length=25)),
                ('colour', models.CharField(default=b'Brown', max_length=30)),
                ('form', models.CharField(default=b'parejo', max_length=20, choices=[(b'parejo', b'Parejo'), (b'torpedo', b'Torpedo'), (b'pyramid', b'Pyramid'), (b'perfecto', b'Perfecto'), (b'presidente', b'Presidente')])),
                ('gauge', models.IntegerField()),
                ('length', models.IntegerField()),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='adarea',
            name='code',
            field=models.CharField(help_text=b'\xe4\xbb\xa3\xe7\xa0\x81', unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='adarea',
            name='description',
            field=models.CharField(help_text=b'\xe6\x8f\x8f\xe8\xbf\xb0', max_length=200),
        ),
        migrations.AlterField(
            model_name='adarea',
            name='status',
            field=models.IntegerField(default=0, help_text=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe6\x9c\x89\xe6\x95\x88'), (0, b'\xe6\x97\xa0\xe6\x95\x88')]),
        ),
        migrations.AlterField(
            model_name='adarea',
            name='title',
            field=models.CharField(help_text=b'\xe6\xa0\x87\xe9\xa2\x98', max_length=100),
        ),
    ]
