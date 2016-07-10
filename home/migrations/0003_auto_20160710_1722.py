# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 11:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='hireme',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 10, 11, 51, 29, 458468, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suggestion',
            name='submit_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 7, 10, 11, 52, 0, 713512, tzinfo=utc)),
            preserve_default=False,
        ),
    ]