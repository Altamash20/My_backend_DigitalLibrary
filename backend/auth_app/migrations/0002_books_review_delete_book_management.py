# Generated by Django 4.0.10 on 2024-12-09 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('ISBN', models.IntegerField()),
                ('Genre', models.CharField(max_length=100)),
                ('Cover_Image_URL', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.PositiveSmallIntegerField()),
                ('Comment', models.CharField(max_length=200)),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.books')),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Book_Management',
        ),
    ]
