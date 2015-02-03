# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatter',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='chatter',
            name='last_name',
        ),
        migrations.AddField(
            model_name='chatter',
            name='full_name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 3, 16, 43, 40, 909828, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
