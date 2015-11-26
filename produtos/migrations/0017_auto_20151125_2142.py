# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0016_remove_produto_especificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='produtos.Categoria', null=True),
        ),
    ]
