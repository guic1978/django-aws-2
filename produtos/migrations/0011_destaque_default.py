# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0010_auto_20151121_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='destaque',
            name='default',
            field=models.BooleanField(default=True, verbose_name=b'Padr\xc3\xa3o'),
        ),
    ]
