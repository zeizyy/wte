# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20160116_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='base',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
    ]
