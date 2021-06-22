from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Book

def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'bookstore/home.html', context)

@login_required
def rent(request, new_pk):
    book = Book.objects.get(pk=new_pk)
    book.status = 'rented'
    book.lent_to = request.user
    book.save()
    return redirect('library-home')

def breturn(request, new_pk):
    book = Book.objects.get(pk=new_pk)
    book.status = 'available'
    book.lent_to = None
    book.save()
    return redirect('library-home')

class BookListView(ListView):
    model = Book
    template_name = 'bookstore/home.html'
    context_object_name = 'books'
    ordering = ['author']

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    context_object_name = 'book'
    fields = ['author','title', 'description']






