from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):
    phone = models.CharField('Номер телефона', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username

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
    memory_size = models.IntegerField('Объем памяти', help_text='в гигабайтах', default=0)
    graphics_processor = models.CharField('Графический процессор', max_length=50, default='')
    memory_bus_bit_depth = models.IntegerField('Битовая глубина шины памяти', default=0)
    num_monitors_connected = models.IntegerField('Количество подключенных мониторов одновременно', default=0)


class Processor(Component):
    socket = models.CharField('Сокет', max_length=20, default='')
    number_cores = models.IntegerField('Количество ядер', validators=[MinValueValidator(1)], default=1)
    ram_type = models.CharField('Тип ОЗУ', max_length=20, default='')

class Motherboard(Component):
    series = models.CharField('Серия', max_length=50)
    socket = models.CharField('Сокет', max_length=20)
    chipset = models.CharField('Чипсет', max_length=50)
    supported_memory_type = models.CharField('Тип поддерживаемой памяти', max_length=50)
    num_memory_slots = models.IntegerField('Количество слотов для памяти')
    num_m2_connectors = models.IntegerField('Количество разъемов M.2')

class Bucket(Component):
    asd = models.CharField('ну надо', max_length=255)