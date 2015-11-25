# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0015_auto_20151125_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='especificacao',
        ),
    ]
