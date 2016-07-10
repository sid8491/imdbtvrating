# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show_rating', '0002_auto_20160706_0121'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpisodeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_title', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=5)),
                ('episode', models.CharField(max_length=5)),
                ('episode_name', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('raters', models.CharField(max_length=10)),
                ('synopsis', models.TextField()),
                ('airdate', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SeasonDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=5)),
                ('total_episodes', models.CharField(max_length=5)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShowDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('imdb_id', models.CharField(blank=True, max_length=20, null=True)),
                ('rating', models.CharField(blank=True, max_length=10, null=True)),
                ('raters', models.CharField(blank=True, max_length=10, null=True)),
                ('total_seasons', models.CharField(blank=True, max_length=5, null=True)),
                ('story', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Show',
        ),
        migrations.DeleteModel(
            name='Show_details',
        ),
        migrations.AddField(
            model_name='seasondetail',
            name='show_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_rating.ShowDetail'),
        ),
        migrations.AddField(
            model_name='episodedetail',
            name='show_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='show_rating.SeasonDetail'),
        ),
    ]