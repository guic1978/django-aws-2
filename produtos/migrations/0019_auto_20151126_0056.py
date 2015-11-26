# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0018_auto_20151125_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='mostra_menu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='categoria',
            name='ordem_menu',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name=b'Categoria Pai', blank=True, to='produtos.Categoria', null=True),
        ),
    ]
