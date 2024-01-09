from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('account', views.account, name = 'account'),
    path('basket', views.basket, name = 'basket'),
    path('registration', views.registration, name = 'registration'),
    path('motherboard', views.motherboard_list, name = 'motherboard'),
    path('videocard', views.videocard_list, name = 'videocard'),
    path('processor', views.processor_list, name = 'processor')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)