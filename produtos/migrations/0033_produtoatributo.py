# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0032_auto_20151201_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoAtributo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atributo', models.ForeignKey(to='produtos.Atributo', unique=True)),
                ('produto', models.ForeignKey(to='produtos.Produto', unique=True)),
                ('valor_item_atributo', models.ForeignKey(verbose_name=b'valor', blank=True, to='produtos.ItemAtributo', null=True)),
            ],
        ),
    ]
