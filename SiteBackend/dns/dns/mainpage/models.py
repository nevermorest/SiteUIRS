from django.db import models
from django.contrib.auth.models import AbstractUser
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

class Processor(Component):
    cores = models.IntegerField('Количество ядер')
    clock_speed = models.DecimalField('Тактовая частота', max_digits=5, decimal_places=2)
    socket = models.CharField('Сокет', max_length=20)