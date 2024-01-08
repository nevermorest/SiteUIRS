from django.shortcuts import render
from .models import VideoCard


def account(request):
    return render(request, 'mainpage/login_page.html')

def basket(request):
    return render(request, 'mainpage/index.html')

def registration(request):
    return render(request, 'mainpage/registration_page.html')

def index(request):
    video_cards = VideoCard.objects.all()
    return render(request, 'mainpage/main_page.html', {'video_cards': video_cards})