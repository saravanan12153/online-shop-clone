# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20160729_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='img/nopic.png', upload_to='products/'),
        ),
    ]