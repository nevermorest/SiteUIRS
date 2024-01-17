# Generated by Django 5.0.1 on 2024-01-16 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0011_remove_motherboard_toslink_spdif_optical'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('image', models.ImageField(upload_to='component_images/', verbose_name='Изображение')),
                ('asd', models.CharField(max_length=255, verbose_name='ну надо')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
