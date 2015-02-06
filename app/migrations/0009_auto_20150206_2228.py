# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20150204_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatter',
            name='device_token',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 6, 22, 28, 8, 275231, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
