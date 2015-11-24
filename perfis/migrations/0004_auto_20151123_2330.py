# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_usuariostripe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariostripe',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='UsuarioStripe',
        ),
    ]
