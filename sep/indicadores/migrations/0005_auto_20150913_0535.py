# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicadores', '0004_auto_20150912_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PorcentajeMujeresIngenieria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entidad', models.CharField(max_length=100)),
                ('ciclo', models.CharField(max_length=50)),
                ('mujeres', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='eficienciaterminal',
            name='eficiencia_terminal',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True),
        ),
    ]
