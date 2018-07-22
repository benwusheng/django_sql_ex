# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-22 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bookinfo',
            managers=[
                ('objs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='heroinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='books', verbose_name='英雄头像'),
        ),
    ]
