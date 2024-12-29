from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def index(request):
    context = {
        'book': Book.objects.all()
    }
    return render(request, 'pages/index.html', context)
def books(request):
    return render(request, 'pages/books.html')

def json(request):
    data = list(Book.objects.values())
    return JsonResponse(data, safe=False)
