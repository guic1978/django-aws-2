# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20151128_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='ativo',
            field=models.BooleanField(default=0),
        ),
    ]
