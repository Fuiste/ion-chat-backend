# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20150212_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatter',
            name='device_token',
            field=models.CharField(default=b'no token', max_length=400),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 22, 35, 19, 803101, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
