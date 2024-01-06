from django.shortcuts import render
def index(request):
    return render(request, 'mainpage/index.html')

def account(request):
    return render(request, 'mainpage/index.html')

def basket(request):
    return render(request, 'mainpage/index.html')