# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150206_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatter',
            name='device_token',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 10, 15, 52, 58, 738518, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
