# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0014_auto_20151125_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriabannerimagem',
            name='imagem',
            field=models.ImageField(upload_to=b'produtos/image/', null=True, verbose_name=b'Imagem (453x154)', blank=True),
        ),
        migrations.AlterField(
            model_name='categoriaimagem',
            name='imagem',
            field=models.ImageField(upload_to=b'produtos/image/', null=True, verbose_name=b'Imagem (100x100)', blank=True),
        ),
    ]
