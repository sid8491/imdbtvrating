# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 19:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('show_rating', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shows',
            new_name='Show',
        ),
    ]
