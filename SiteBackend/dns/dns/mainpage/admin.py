from django.contrib import admin
from .models import VideoCard, Processor, Motherboard, Bucket
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Добавляем поле 'phone' в форму добавления пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'phone'),
        }),
    )

# Регистрируем модель User с нашим пользовательским администратором
admin.site.register(User, CustomUserAdmin)
admin.site.register(VideoCard)
admin.site.register(Processor)
admin.site.register(Motherboard)
admin.site.register(Bucket)