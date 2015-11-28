# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20151128_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoItemMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255, verbose_name=b'Item')),
            ],
        ),
        migrations.RemoveField(
            model_name='itemmenu',
            name='paginas',
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='is_link',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='link',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='ordem',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemmenu',
            name='pagina',
            field=models.ForeignKey(blank=True, to='core.Pagina', null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='padrao',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='itemmenu',
            name='menu',
            field=models.ForeignKey(to='core.GrupoItemMenu'),
        ),
        migrations.AlterField(
            model_name='itemmenu',
            name='nome',
            field=models.CharField(max_length=255, verbose_name=b'Item'),
        ),
        migrations.AddField(
            model_name='grupoitemmenu',
            name='menu',
            field=models.ForeignKey(to='core.Menu'),
        ),
    ]
