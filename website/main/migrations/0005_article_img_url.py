# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170309_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img_url',
            field=models.CharField(default='http://www.poker.no/wp-content/uploads/2017/02/Karl-Fredrik-R%C3%B8sok-620x330.jpg', max_length=500),
        ),
    ]
