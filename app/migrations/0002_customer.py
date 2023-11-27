# Generated by Django 4.2.7 on 2023-11-27 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=62, null=True)),
                ('photo_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(default='')),
                ('birtday_day', models.DateField()),
                ('joined_date', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=18), django.core.validators.MaxValueValidator(limit_value=35)])),
                ('username', models.CharField(max_length=64, unique=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
