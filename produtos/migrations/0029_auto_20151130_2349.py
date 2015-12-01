# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0028_produtoatributo_atributo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoatributo',
            name='valor_item_atributo',
            field=models.ForeignKey(verbose_name=b'valor', blank=True, to='produtos.ItemAtributo', null=True),
        ),
    ]
