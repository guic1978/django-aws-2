# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_noticia'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='titulo_curto',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(upload_to=b'produtos/image/', null=True, verbose_name=b'Imagem (420x450)', blank=True),
        ),
    ]
