# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_auto_20160120_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
