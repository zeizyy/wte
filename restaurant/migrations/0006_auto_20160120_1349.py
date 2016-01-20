# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_userprofile_base'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
