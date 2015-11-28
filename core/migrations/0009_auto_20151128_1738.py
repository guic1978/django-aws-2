# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20151128_0353'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('local', models.CharField(blank=True, max_length=20, null=True, choices=[(b'HEADER', b'HEADER'), (b'FOOTER', b'FOOTER'), (b'MOBILE', b'MOBILE')])),
            ],
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255, null=True, blank=True)),
                ('slug', models.SlugField()),
                ('conteudo', tinymce.models.HTMLField(null=True, verbose_name=b'Conte\xc3\xbado', blank=True)),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Alterado')),
            ],
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='menu',
            field=models.ForeignKey(to='core.Menu'),
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='paginas',
            field=models.ManyToManyField(to='core.Pagina', null=True, blank=True),
        ),
    ]
