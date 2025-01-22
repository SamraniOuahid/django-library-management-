from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from .models import *
from .models import Book, Category
from .forms import BookForm, CategoryForm

# Create your views here.
# index
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
        'allbooks': Book.objects.filter(active=True).count(),
        'booksold': Book.objects.filter(status='sold').count(),
        'bookrental': Book.objects.filter(status='rental').count(),
        'bookavailable': Book.objects.filter(status='available').count(),
        # 'booksold': Book.objects.filter(title=='sold').count(),
    }
    return render(request, 'pages/index.html', context)

# veiw of book
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

# view of update book
def update(request, id):
    book_id = Book.objects.get(id = id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    context = {
        'form': book_save,
    }
    return render(request, 'pages/update.html', context)

# delete
def delete(request, id):
    book_id = get_object_or_404(Book, id = id)
    if request.method == 'POST':
        book_id.delete()
        return redirect('/')
    return render(request, 'pages/delet.html')

# return format json
def json(request):
    data = list(Book.objects.values())
    return JsonResponse(data, safe=False)
