# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 06:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170312_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='Article_image',
        ),
    ]