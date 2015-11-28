# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20151127_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='conteudo',
            field=tinymce.models.HTMLField(null=True, verbose_name=b'Conte\xc3\xbado', blank=True),
        ),
    ]
