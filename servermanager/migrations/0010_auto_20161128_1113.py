# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-28 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servermanager', '0009_auto_20161128_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='nic',
            field=models.ManyToManyField(blank=True, null=True, to='servermanager.NIC', verbose_name='\u7f51\u5361\u5217\u8868'),
        ),
    ]