# Generated by Django 4.1.5 on 2023-03-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilmhub_app', '0005_merge_20230306_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='audio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='has_image',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='studentlesson',
            name='status',
            field=models.TextField(choices=[('Assigned', 'Assigned'), ('Completed', 'Completed'), ('Confirmed', 'Confirmed'), ('Marked For Redo', 'Marked For Redo')], default='Assigned'),
        ),
    ]