from django.shortcuts import render
from .models import VideoCard, Motherboard, Processor

def index(request):
    video_cards = VideoCard.objects.all()
    return render(request, 'mainpage/main_page.html', {'components': video_cards})

def account(request):
    return render(request, 'mainpage/login_page.html')

def basket(request):
    return render(request, 'mainpage/index.html')

def registration(request):
    return render(request, 'mainpage/registration_page.html')

def motherboard_list(request):
    motherboards = Motherboard.objects.all()
    return render(request, 'mainpage/main_page.html', {'components': motherboards})

def videocard_list(request):
    video_cards = VideoCard.objects.all()
    return render(request, 'mainpage/main_page.html', {'components': video_cards})

def processor_list(request):
    processor = Processor.objects.all()
    return render(request, 'mainpage/main_page.html', {'components': processor})