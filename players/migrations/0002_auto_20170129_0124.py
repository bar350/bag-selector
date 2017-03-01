# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bgg_username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='board_games',
            field=models.ManyToManyField(blank=True, related_name='owned_by', to='boardgames.BoardGame'),
        ),
        migrations.AlterField(
            model_name='player',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='members', to='players.GameGroup'),
        ),
    ]