# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-08-16 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20190816_0631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.Ingredient'),
        ),
    ]
