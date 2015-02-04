# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150204_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='msg_from',
        ),
        migrations.AddField(
            model_name='message',
            name='msg_to',
            field=models.ForeignKey(related_name='Message_msg_to', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 4, 15, 53, 7, 17824, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
