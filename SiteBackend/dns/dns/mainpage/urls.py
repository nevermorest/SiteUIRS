from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('account', views.account, name = 'account'),
    path('basket', views.basket, name = 'basket'),
    path('registration', views.registration, name = 'registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)