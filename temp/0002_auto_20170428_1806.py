# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapi.Book')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='author',
        ),
        migrations.AddField(
            model_name='user',
            name='favourites',
            field=models.ManyToManyField(to='bookapi.Category'),
        ),
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(to='bookapi.Author'),
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='users_likes', to='bookapi.Book'),
        ),
        migrations.AddField(
            model_name='user',
            name='read',
            field=models.ManyToManyField(related_name='users_read', to='bookapi.Book'),
        ),
        migrations.AddField(
            model_name='user',
            name='wishes',
            field=models.ManyToManyField(related_name='users_wishes', to='bookapi.Book'),
        ),
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapi.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='rated',
            field=models.ManyToManyField(related_name='users_rated', through='bookapi.Rate', to='bookapi.Book'),
        ),
    ]
