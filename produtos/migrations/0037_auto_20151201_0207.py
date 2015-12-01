# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0036_auto_20151201_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoatributo',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto', primary_key=True),
        ),
    ]
