# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='street_addr',
            field=models.CharField(default=b'SOME STRING', max_length=30),
        ),
    ]