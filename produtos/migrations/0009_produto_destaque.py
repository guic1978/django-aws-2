# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_auto_20151121_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='destaque',
            field=models.BooleanField(default=False),
        ),
    ]
