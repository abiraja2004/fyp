# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_post_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('quotation', models.TextField(blank=True)),
                ('speaker', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('post', models.ForeignKey(to='news.Post')),
            ],
        ),
    ]
