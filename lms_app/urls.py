from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('json/', views.json, name='json'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]