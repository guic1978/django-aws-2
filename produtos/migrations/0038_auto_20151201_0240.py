# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0037_auto_20151201_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtoatributo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=None, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produtoatributo',
            name='atributo',
            field=models.ForeignKey(to='produtos.Atributo'),
        ),
        migrations.AlterField(
            model_name='produtoatributo',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto'),
        ),
        migrations.AlterUniqueTogether(
            name='produtoatributo',
            unique_together=set([('produto', 'atributo')]),
        ),
    ]
