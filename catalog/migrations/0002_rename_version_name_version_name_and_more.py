# Generated by Django 4.2.5 on 2023-10-07 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='version_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='version_number',
            new_name='number',
        ),
    ]
