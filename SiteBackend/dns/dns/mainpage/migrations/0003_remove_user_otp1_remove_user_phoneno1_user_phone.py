# Generated by Django 5.0.1 on 2024-01-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='otp1',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phoneno1',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона'),
        ),
    ]