# Generated by Django 4.1.5 on 2023-03-18 23:57

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilmhub_app', '0007_merge_20230318_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='audio',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='media/'), upload_to=''),
        ),
    ]