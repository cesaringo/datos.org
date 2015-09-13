# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0005_auto_20150913_0535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('programa', models.CharField(max_length=200)),
                ('institucion', models.CharField(max_length=200)),
                ('entidad_federativa', models.CharField(max_length=100)),
                ('clave_entidad', models.IntegerField()),
                ('sostenimiento', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
    ]
