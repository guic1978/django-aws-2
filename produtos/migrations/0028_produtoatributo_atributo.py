# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0027_remove_produtoatributo_atributo'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtoatributo',
            name='atributo',
            field=models.ForeignKey(default=0, to='produtos.Atributo'),
            preserve_default=False,
        ),
    ]
