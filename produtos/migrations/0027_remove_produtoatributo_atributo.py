# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0026_auto_20151129_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtoatributo',
            name='atributo',
        ),
    ]
