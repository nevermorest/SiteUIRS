from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h4>пися попа</h4>")
# Create your views here.
