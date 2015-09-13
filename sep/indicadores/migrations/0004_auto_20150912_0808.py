# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0003_auto_20150912_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eficienciaterminal',
            name='egresados',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='eficienciaterminal',
            name='nivel_educativo',
            field=models.CharField(max_length=50, choices=[(b'01 PRESCOLAR', b'PRESCOLAR'), (b'02 PRIMARIA', b'PRIMARIA'), (b'03 SECUNDARIA', b'SECUNDARIA'), (b'05 MEDIA SUPERIOR', b'MEDIA SUPERIOR'), (b'06 SUPERIOR', b'SUPERIOR')]),
        ),
        migrations.AlterField(
            model_name='eficienciaterminal',
            name='nuevos_ingresos',
            field=models.IntegerField(null=True),
        ),
    ]
