# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20160726_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='picture',
            field=models.ImageField(default='static/img/nopic.png', upload_to='stores/'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_type',
            field=models.CharField(choices=[('education', 'Education'), ('fashion', 'Fashion'), ('food', 'Food'), ('furniture', 'Furniture'), ('electronics', 'Electronics'), ('beauty', 'Beauty'), ('No category set', '')], max_length=25),
        ),
    ]
