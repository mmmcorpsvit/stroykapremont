# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 20:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0004_auto_20180222_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='desc',
            field=models.CharField(max_length=150),
        ),
    ]
