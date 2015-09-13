# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eficienciaterminal',
            old_name='entidad',
            new_name='entidad_federativa',
        ),
    ]
