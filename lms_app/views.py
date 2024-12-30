from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from .forms import BookForm, CategoryForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST, request.FILES)
        if add_category.is_valid():
            add_category.save()
    context = {
        'book': Book.objects.all(),
        'category': Category.objects.all(),
        'forms': BookForm(),
        'formscat': CategoryForm(),
    }
    return render(request, 'pages/index.html', context)
def books(request):
    if request.method == 'POST':
        add_category = CategoryForm(request.POST, request.FILES)
        if add_category.is_valid():
            add_category.save()
    context = {
        'book': Book.objects.all(),
        'category': Category.objects.all(),
        'formscat': CategoryForm(),
    }
    return render(request, 'pages/books.html', context)

def update(request):
    return render(request, 'pages/update.html')

def json(request):
    data = list(Book.objects.values())
    return JsonResponse(data, safe=False)
