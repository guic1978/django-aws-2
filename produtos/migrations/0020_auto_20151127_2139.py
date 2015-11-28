# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0019_auto_20151126_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='produto',
            new_name='produtos',
        ),
    ]
