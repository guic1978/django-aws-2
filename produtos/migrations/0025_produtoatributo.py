# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0024_itematributo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutoAtributo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_char', models.CharField(max_length=50, null=True, blank=True)),
                ('atributo', models.ForeignKey(to='produtos.Atributo')),
                ('produto', models.ForeignKey(to='produtos.Produto')),
                ('valor_item_atributo', models.ForeignKey(blank=True, to='produtos.ItemAtributo', null=True)),
            ],
        ),
    ]
