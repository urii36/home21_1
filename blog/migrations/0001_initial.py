# Generated by Django 4.2.5 on 2023-09-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('content', models.TextField()),
                ('preview_image', models.ImageField(upload_to='blog_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
                ('views_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]