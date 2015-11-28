# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20151128_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupoitemmenu',
            name='menu',
        ),
        migrations.AddField(
            model_name='grupoitemmenu',
            name='menu',
            field=models.ManyToManyField(to='core.Menu'),
        ),
    ]
