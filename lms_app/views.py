from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def index(request):
    context = {
        'book': Book.objects.all(),
        'category': Category.objects.all(),
    }
    return render(request, 'pages/index.html', context)
def books(request):
    context = {
        'book': Book.objects.all(),
        'category': Category.objects.all(),
    }
    return render(request, 'pages/books.html', context)

def json(request):
    data = list(Book.objects.values())
    return JsonResponse(data, safe=False)
