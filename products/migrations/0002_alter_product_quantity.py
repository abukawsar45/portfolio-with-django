# Generated by Django 5.0.1 on 2024-02-01 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.TextField(blank=True, null=True),
        ),
    ]
