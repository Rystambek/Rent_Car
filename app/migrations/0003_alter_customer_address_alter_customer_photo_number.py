# Generated by Django 4.2.7 on 2023-11-27 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='photo_number',
            field=models.CharField(max_length=13),
        ),
    ]
