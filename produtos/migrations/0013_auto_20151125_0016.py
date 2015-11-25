# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0012_auto_20151122_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriaimagem',
            name='imagem_banner',
            field=models.ImageField(upload_to=b'produtos/image/', null=True, verbose_name=b'Imagem (453x154)', blank=True),
        ),
        migrations.AlterField(
            model_name='categoriaimagem',
            name='imagem',
            field=models.ImageField(upload_to=b'produtos/image/', null=True, verbose_name=b'Imagem (60x60)', blank=True),
        ),
        migrations.AlterField(
            model_name='produtoimagem',
            name='imagem',
            field=models.ImageField(upload_to=b'produtos/image/', verbose_name=b'Imagem (420x450)'),
        ),
    ]
