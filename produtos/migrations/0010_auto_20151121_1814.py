# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_produto_destaque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destaque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=120)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Alterado')),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='destaque',
        ),
        migrations.AlterField(
            model_name='produto',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='destaque',
            name='produtos',
            field=models.ManyToManyField(to='produtos.Produto', null=True, blank=True),
        ),
    ]
