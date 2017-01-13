# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 6, 13, 3, 50, 667664, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
