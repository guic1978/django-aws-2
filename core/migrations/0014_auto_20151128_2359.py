# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20151128_1850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupoitemmenu',
            options={'ordering': ['ordem']},
        ),
        migrations.AlterModelOptions(
            name='itemmenu',
            options={'ordering': ['ordem']},
        ),
        migrations.AddField(
            model_name='grupoitemmenu',
            name='ordem',
            field=models.SmallIntegerField(default=0),
        ),
    ]
