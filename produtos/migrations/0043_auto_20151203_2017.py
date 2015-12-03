# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0042_auto_20151202_0024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriabannerimagem',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='categoriaimagem',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='CategoriaBannerImagem',
        ),
        migrations.DeleteModel(
            name='CategoriaImagem',
        ),
    ]
