# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0022_auto_20151129_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='atributo',
            name='tipo',
            field=models.CharField(default=b'CAMPO_TEXTO', max_length=35, choices=[(b'CAMPO_TEXTO', b'CAMPO_TEXTO'), (b'SELECAO', b'SELECAO')]),
        ),
    ]
