# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0033_produtoatributo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtoatributo',
            name='atributo',
            field=models.OneToOneField(to='produtos.Atributo'),
        ),
        migrations.AlterField(
            model_name='produtoatributo',
            name='produto',
            field=models.OneToOneField(to='produtos.Produto'),
        ),
    ]
