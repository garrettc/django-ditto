# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0041_remove_media_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='tweets',
            field=models.ManyToManyField(related_name='media', to='twitter.Tweet'),
        ),
    ]
