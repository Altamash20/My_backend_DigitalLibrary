# Generated by Django 4.0.10 on 2024-12-09 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('ISBN', models.IntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('cover_image_URL', models.URLField(default='')),
            ],
        ),
    ]
