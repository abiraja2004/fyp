# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20170126_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='LSA',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='featured_lexrank',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='lexrank',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='sum_basic',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='textrank',
            field=models.TextField(blank=True),
        ),
    ]
