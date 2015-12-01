# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0025_produtoatributo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atributo',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='produtoatributo',
            name='valor_char',
        ),
    ]
