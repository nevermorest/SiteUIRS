from django.shortcuts import render
from .models import VideoCard, Motherboard, Processor, Bucket
from django.contrib.auth.decorators import login_required
from .forms import SearchForm

def index(request):
    video_cards = VideoCard.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        video_cards = video_cards.filter(name__icontains=search_text)

    return render(request, 'mainpage/main_page.html', {'components': video_cards, 'search_form': search_form})


def custom_login(request):
    return render(request, 'mainpage/login_page.html')

def basket(request):
    basket = Bucket.objects.all()

    return render(request, 'mainpage/bucket_page.html', {'components': basket})

def registration(request):
    return render(request, 'mainpage/registration_page.html')

def motherboard_list(request):
    motherboard = Motherboard.objects.all()
    search_form = SearchForm(request.GET)
    number = 2

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        motherboard = motherboard.filter(name__icontains=search_text)

    return render(request, 'mainpage/main_page.html', {'components': motherboard, 'search_form': search_form, 'number': number})

def videocard_list(request):
    video_cards = VideoCard.objects.all()
    search_form = SearchForm(request.GET)
    number = 1

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        video_cards = video_cards.filter(name__icontains=search_text)

    return render(request, 'mainpage/main_page.html', {'components': video_cards, 'search_form': search_form, 'number': number})  

def processor_list(request):
    processor = Processor.objects.all()
    search_form = SearchForm(request.GET)
    number = 3

    if search_form.is_valid():
        search_text = search_form.cleaned_data['search_text']
        processor = processor.filter(name__icontains=search_text)

    return render(request, 'mainpage/main_page.html', {'components': processor, 'search_form': search_form, 'number': number})

@login_required
def profile_view(request):
    return render(request, 'mainpage/profile.html')