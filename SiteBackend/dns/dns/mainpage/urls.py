from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'home'),
    path('account', views.account, name = 'account'),
    path('basket', views.basket, name = 'basket'),
    path('registration', views.registration, name = 'registration')
]
