# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='restaurant',
            field=models.ManyToManyField(to='restaurant.Restaurant'),
        ),
    ]
