# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150203_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='created_at',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
