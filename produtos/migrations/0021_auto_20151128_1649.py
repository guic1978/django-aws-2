# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0020_auto_20151127_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True),
        ),
    ]
