# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20151128_1844'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemmenu',
            old_name='menu',
            new_name='grupo_menu',
        ),
    ]
