# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0031_auto_20151130_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtoatributo',
            name='atributo',
        ),
        migrations.RemoveField(
            model_name='produtoatributo',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='produtoatributo',
            name='valor_item_atributo',
        ),
        migrations.DeleteModel(
            name='ProdutoAtributo',
        ),
    ]
