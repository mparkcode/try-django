from django.shortcuts import render
from .models import Book

# Create your views here.
def get_index(request):
    books = Book.objects.all()
    return render(request, "home/index.html", {'books':books})