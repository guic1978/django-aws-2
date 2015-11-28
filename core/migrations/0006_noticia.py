# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20151116_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('conteudo', models.TextField(null=True, verbose_name=b'Conte\xc3\xbado', blank=True)),
                ('data_publicacao', models.DateTimeField()),
                ('data_expiracao', models.DateTimeField()),
                ('ativo', models.BooleanField(default=True)),
                ('destaque', models.BooleanField(default=False)),
                ('imagem', models.ImageField(upload_to=b'produtos/image/', verbose_name=b'Imagem (420x450)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Alterado')),
                ('autor', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-data_publicacao'],
            },
        ),
    ]
