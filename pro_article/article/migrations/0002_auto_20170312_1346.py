# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 05:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Article_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='img', verbose_name='图片'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='Article_text',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='Article_url',
            field=models.CharField(max_length=100, verbose_name='链接'),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.CharField(max_length=100, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='article',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Categary', verbose_name='栏目'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=500, verbose_name='正文'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='categary',
            name='Categary_text',
            field=models.CharField(max_length=50, verbose_name='栏目名'),
        ),
    ]
