# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-01 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0054_auto_20170101_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officialaccount',
            name='wx_id',
            field=models.CharField(max_length=100, unique=True, verbose_name='\u516c\u4f17\u53f7\u5fae\u4fe1ID'),
        ),
    ]