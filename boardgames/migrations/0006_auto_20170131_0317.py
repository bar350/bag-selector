# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardgames', '0005_boardgame_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgame',
            name='boardgame_rank',
            field=models.FloatField(blank=True, null=True),
        ),
    ]