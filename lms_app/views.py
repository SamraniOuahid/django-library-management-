from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
def books(request):
    return render(request, 'pages/books.html')

def json(request):
    data = list(Book.objects.values())
    return JsonResponse(data, safe=False)
