# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_quotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='post',
            field=models.ForeignKey(related_name='quotation', to='news.Post'),
        ),
    ]
