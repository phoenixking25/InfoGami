# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-10 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_remove_createusergroupmodel_group_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createusergroupmodel',
            name='group_status',
            field=models.CharField(default='open', max_length=15),
        ),
    ]