# Generated by Django 4.2.7 on 2023-11-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('url', models.URLField(unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('price', models.FloatField()),
                ('color', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('years', models.IntegerField()),
                ('motors', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
