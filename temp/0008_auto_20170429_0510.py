# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0007_auto_20170429_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='pics/'),
        ),
    ]