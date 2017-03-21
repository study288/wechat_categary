# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Article_text', models.CharField(max_length=50)),
                ('Article_url', models.CharField(max_length=100)),
                ('abstract', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Categary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categary_text', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Categary'),
        ),
    ]