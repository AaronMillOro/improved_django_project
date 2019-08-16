# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2019-08-16 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20190816_0629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='item',
            name='ingredients',
            field=models.ManyToManyField(to='menu.Ingredient'),
        ),
        migrations.RemoveField(
            model_name='menu',
            name='items',
        ),
        migrations.AddField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(related_name='items', to='menu.Item'),
        ),
    ]
