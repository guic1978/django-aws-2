# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import produtos.models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_auto_20151111_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='download',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/opt/bitnami/apps/django/django_projects/Project/core/protegido'), null=True, upload_to=produtos.models.local_download, blank=True),
        ),
    ]
