# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-01 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5'),
        ),
    ]