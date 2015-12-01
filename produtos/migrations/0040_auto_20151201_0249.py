# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0039_auto_20151201_0247'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoAtributo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atributo', models.ForeignKey(to='produtos.Atributo')),
                ('produto', models.ForeignKey(to='produtos.Produto')),
                ('valor_item_atributo', models.ForeignKey(verbose_name=b'valor', blank=True, to='produtos.ItemAtributo', null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='produtoatributo',
            unique_together=set([('produto', 'atributo')]),
        ),
    ]
