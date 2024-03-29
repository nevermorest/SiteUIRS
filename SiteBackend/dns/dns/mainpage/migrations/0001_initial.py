# Generated by Django 5.0.1 on 2024-01-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('image', models.ImageField(upload_to='component_images/', verbose_name='Изображение')),
                ('cores', models.IntegerField(verbose_name='Количество ядер')),
                ('clock_speed', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Тактовая частота')),
                ('socket', models.CharField(max_length=20, verbose_name='Сокет')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('image', models.ImageField(upload_to='component_images/', verbose_name='Изображение')),
                ('memory_size', models.IntegerField(help_text='в гигабайтах', verbose_name='Объем памяти')),
                ('chipset', models.CharField(max_length=50, verbose_name='Чипсет')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
