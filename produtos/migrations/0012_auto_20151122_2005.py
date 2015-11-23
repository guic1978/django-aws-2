# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0011_destaque_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='destaque',
            name='descricao',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='destaque',
            name='default',
            field=models.BooleanField(default=False, verbose_name=b'Padr\xc3\xa3o'),
        ),
    ]
