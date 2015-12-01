# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0021_auto_20151128_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atributo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('nome_display', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('filtra', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AtributoGrupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('atributos', models.ManyToManyField(to='produtos.Atributo')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='grupo_atributo',
            field=models.ForeignKey(blank=True, to='produtos.AtributoGrupo', null=True),
        ),
    ]
