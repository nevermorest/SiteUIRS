# Generated by Django 5.0.1 on 2024-01-16 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0012_bucket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='motherboard',
            name='max_memory_frequency',
        ),
        migrations.RemoveField(
            model_name='motherboard',
            name='overclocked_ram_frequency',
        ),
    ]
