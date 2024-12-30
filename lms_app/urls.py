from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('json/', views.json, name='json'),
    path('<int:id>',views.update, name='update')
   
]