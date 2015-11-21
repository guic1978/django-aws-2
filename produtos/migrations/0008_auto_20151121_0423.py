# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0007_auto_20151121_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='parent',
            field=models.ForeignKey(related_name='child', verbose_name=b'Categoria Pai', blank=True, to='produtos.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='produto',
            field=models.ManyToManyField(to='produtos.Produto', null=True, blank=True),
        ),
    ]
