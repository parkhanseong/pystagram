# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20160312_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Photo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='Photo',
            new_name='photo',
        ),
    ]
