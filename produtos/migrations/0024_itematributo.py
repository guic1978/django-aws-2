# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0023_atributo_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemAtributo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.CharField(max_length=50)),
                ('atributo', models.ForeignKey(to='produtos.Atributo')),
            ],
        ),
    ]
