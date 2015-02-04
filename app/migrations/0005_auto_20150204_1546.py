# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150203_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 4, 15, 46, 34, 253961, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chatter',
            name='imgur_url',
            field=models.CharField(default=b'http://i.imgur.com/23el4Y8.jpg', max_length=400),
            preserve_default=True,
        ),
    ]
