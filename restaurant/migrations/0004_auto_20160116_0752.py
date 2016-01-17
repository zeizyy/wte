# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0003_auto_20160116_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='array',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
