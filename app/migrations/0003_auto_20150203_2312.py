# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150203_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatter',
            name='imgur_url',
            field=models.CharField(default=b'http://imgur.com/23el4Y8', max_length=400),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 3, 23, 12, 1, 219851, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
