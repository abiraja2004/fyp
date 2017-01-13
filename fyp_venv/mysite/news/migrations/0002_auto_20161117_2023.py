# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='fivelinesummary',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tenlinesummary',
            field=models.TextField(blank=True),
        ),
    ]
