# Generated by Django 5.0.1 on 2024-02-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verify_key',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
