# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-24 10:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_expensephoto_claim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseclaim',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expensephoto',
            name='claim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='expenses.ExpenseClaim'),
        ),
    ]
