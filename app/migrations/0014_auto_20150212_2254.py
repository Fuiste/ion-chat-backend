# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20150212_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatter',
            name='device_type',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 22, 54, 6, 197758, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
