# Generated by Django 5.0.1 on 2024-01-11 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_alter_videocard_standard_clock_speed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motherboard',
            old_name='intel_chipset',
            new_name='chipset',
        ),
    ]
