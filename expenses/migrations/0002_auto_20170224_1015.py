# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensephoto',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
