# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-15 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_userfavorite_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomments',
            name='comments',
            field=models.CharField(max_length=400, verbose_name='\u8bc4\u8bba'),
        ),
    ]