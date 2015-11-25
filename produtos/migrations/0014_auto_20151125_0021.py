# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0013_auto_20151125_0016'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaBannerImagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagem', models.ImageField(upload_to=b'produtos/image/', verbose_name=b'Imagem (453x154)')),
                ('titulo', models.CharField(max_length=120, null=True, blank=True)),
                ('imagem_principal', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Alterado')),
                ('categoria', models.ForeignKey(to='produtos.Categoria', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='categoriaimagem',
            name='imagem_banner',
        ),
        migrations.AlterField(
            model_name='categoriaimagem',
            name='imagem',
            field=models.ImageField(upload_to=b'produtos/image/', verbose_name=b'Imagem (100x100)'),
        ),
    ]
