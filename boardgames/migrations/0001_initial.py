# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 01:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgame_rank', models.FloatField()),
                ('description', models.TextField()),
                ('bgg_id', models.IntegerField()),
                ('image_url', models.CharField(max_length=300)),
                ('max_players', models.IntegerField()),
                ('min_age', models.IntegerField()),
                ('min_players', models.IntegerField()),
                ('name', models.CharField(max_length=400)),
                ('playing_time', models.IntegerField()),
                ('rating_average', models.FloatField()),
                ('rating_bayes_average', models.FloatField()),
                ('thumbnail_url', models.CharField(max_length=300)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GameMechanic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mechanic', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerSuggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_count', models.CharField(max_length=3)),
                ('recommended', models.IntegerField()),
                ('not_recommended', models.IntegerField()),
                ('best', models.IntegerField()),
                ('board_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players_suggestions', to='boardgames.BoardGame')),
            ],
        ),
        migrations.AddField(
            model_name='boardgame',
            name='categories',
            field=models.ManyToManyField(to='boardgames.GameCategory'),
        ),
        migrations.AddField(
            model_name='boardgame',
            name='mechanics',
            field=models.ManyToManyField(to='boardgames.GameMechanic'),
        ),
    ]
