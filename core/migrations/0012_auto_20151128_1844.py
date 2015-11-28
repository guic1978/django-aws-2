# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20151128_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupoitemmenu',
            old_name='menu',
            new_name='menus',
        ),
    ]
