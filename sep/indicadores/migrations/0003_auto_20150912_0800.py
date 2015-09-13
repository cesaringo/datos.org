# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0002_auto_20150912_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eficienciaterminal',
            name='eficiencia_terminal',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=1, blank=True),
        ),
        migrations.AlterField(
            model_name='eficienciaterminal',
            name='nivel_educativo',
            field=models.CharField(max_length=50, choices=[(b'01 PRESCOLAR', b'PRESCOLAR'), (b'02 PRIMARIA', b'PRIMARIA'), (b'03 SECUNDARIA', b'SECUNDARIA'), (b'04 MEDIA SUPERIOR', b'MEDIA SUPERIOR'), (b'05 SUPERIOR', b'SUPERIOR')]),
        ),
    ]
