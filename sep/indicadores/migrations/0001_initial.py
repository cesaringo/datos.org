# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EficienciaTerminal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entidad', models.CharField(max_length=100)),
                ('nivel_educativo', models.CharField(max_length=50, choices=[(b'PRESCOLAR', b'PRESCOLAR'), (b'PRIMARIA', b'PRIMARIA'), (b'SECUNDARIA', b'SECUNDARIA'), (b'MEDIA SUPERIOR', b'MEDIA SUPERIOR'), (b'SUPERIOR', b'SUPERIOR')])),
                ('servicio_educativo', models.CharField(max_length=100)),
                ('num_municipio', models.IntegerField()),
                ('nombre_municipio', models.CharField(max_length=100)),
                ('ciclo_escolar', models.CharField(max_length=50)),
                ('nuevos_ingresos', models.IntegerField()),
                ('egresados', models.IntegerField()),
                ('eficiencia_terminal', models.DecimalField(max_digits=4, decimal_places=1)),
            ],
        ),
    ]
