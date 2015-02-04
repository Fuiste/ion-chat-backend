# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150204_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatter',
            name='message_history',
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 4, 16, 28, 35, 412516, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
