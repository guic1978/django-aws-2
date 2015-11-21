# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import produtos.models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0006_auto_20151119_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='parent',
            field=models.ForeignKey(related_name='Children', verbose_name=b'Categoria Pai', blank=True, to='produtos.Categoria', null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='download',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/guilhermereis/PycharmProjects/encontreaqui/core/protegido'), null=True, upload_to=produtos.models.local_download, blank=True),
        ),
    ]
