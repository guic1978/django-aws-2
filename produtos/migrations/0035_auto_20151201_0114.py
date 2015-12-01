# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0034_auto_20151201_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='grupo_atributo',
            field=models.ForeignKey(default=0, to='produtos.AtributoGrupo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produtoatributo',
            name='atributo',
            field=models.ForeignKey(to='produtos.Atributo', unique=True),
        ),
        migrations.AlterField(
            model_name='produtoatributo',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto', unique=True),
        ),
    ]
