# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hireme',
            name='comments',
            field=models.TextField(default='hire me'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hireme',
            name='email',
            field=models.EmailField(default='sid.anything.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='email',
            field=models.EmailField(default='sid.anything.com', max_length=254),
            preserve_default=False,
        ),
    ]
