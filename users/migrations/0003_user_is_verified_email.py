# Generated by Django 4.2.5 on 2023-10-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified_email',
            field=models.BooleanField(default=False),
        ),
    ]