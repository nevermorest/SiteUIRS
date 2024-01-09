from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models

class User(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

# Добавим related_name для связей с группами и правами
User._meta.get_field('groups').remote_field.related_name = 'mainpage_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'mainpage_user_user_permissions'

class Component(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.IntegerField('Количество')
    image = models.ImageField('Изображение', upload_to='component_images/')

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name
    
class VideoCard(Component):
    memory_size = models.IntegerField('Объем памяти', help_text='в гигабайтах')
    chipset = models.CharField('Чипсет', max_length=50)

    #
    #
    #
    #
    #
    #
    #
    #
    #

class Processor(models.Model):
    socket = models.CharField('Сокет', max_length=20)
    release_year = models.IntegerField('Год релиза', validators=[MinValueValidator(1900)])
    cores = models.IntegerField('Количество ядер', validators=[MinValueValidator(1)])
    threads = models.IntegerField('Количество потоков', validators=[MinValueValidator(1)])
    l2_cache_size = models.CharField('Размер кэша L2', max_length=20)
    l3_cache_size = models.CharField('Размер кэша L3', max_length=20)
    technical_process = models.CharField('Техпроцесс', max_length=20)
    core = models.CharField('Ядро', max_length=20)
    clock_speed = models.DecimalField('Тактовая частота', max_digits=5, decimal_places=2)
    max_clock_speed = models.DecimalField('Максимальная тактовая частота', max_digits=5, decimal_places=2)
    ram_type = models.CharField('Тип ОЗУ', max_length=20)
    max_ram = models.CharField('Максимальный объем ОЗУ', max_length=20)
    num_channels = models.IntegerField('Количество каналов памяти', validators=[MinValueValidator(1)])
    heat_release = models.CharField('Тепловыделение', max_length=20)
    max_temperature = models.DecimalField('Максимальная температура процессора', max_digits=5, decimal_places=2)
    virtualization = models.BooleanField('Виртуализация')



class motherboard(Component):
    memory_size = models.IntegerField('Объем памяти', help_text='в гигабайтах')
    chipset = models.CharField('Чипсет', max_length=50)

class Cooling(Component):
    memory_size = models.IntegerField('Объем памяти', help_text='в гигабайтах')
    chipset = models.CharField('Чипсет', max_length=50)

class corpus(Component):
    memory_size = models.IntegerField('Объем памяти', help_text='в гигабайтах')
    chipset = models.CharField('Чипсет', max_length=50)

class RAM(Component):
    memory_size = models.IntegerField('Объем памяти', help_text='в гигабайтах')
    chipset = models.CharField('Чипсет', max_length=50)

class SoundСard(Component):
    memory_size = models.IntegerField('Объем памяти', help_text='в гигабайтах')
    chipset = models.CharField('Чипсет', max_length=50)
