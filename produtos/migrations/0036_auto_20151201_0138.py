# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0035_auto_20151201_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtoatributo',
            name='id',
        ),
        migrations.AlterField(
            model_name='produtoatributo',
            name='atributo',
            field=models.ForeignKey(primary_key=True, serialize=False, to='produtos.Atributo'),
        ),
        migrations.AlterField(
            model_name='produtoatributo',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto', primary_key=True),
        ),
    ]
