# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 22:28
from __future__ import unicode_literals

import activos_fijos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos_fijos', '0004_auto_20170912_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activofijo',
            name='fecha_compra',
            field=models.DateTimeField(blank=True, null=True, validators=[activos_fijos.validators.validate_fecha_compra]),
        ),
    ]