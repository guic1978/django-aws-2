# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0030_auto_20151130_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtoatributo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=0, serialize=False, verbose_name='ID'),
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
