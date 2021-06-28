from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Book

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

class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    permission_required = 'bookstore.add_book'
    
    model = Book
    context_object_name = 'book'
    fields = ['author','title', 'description']

    def handle_no_permission(self):
        messages.warning(self.request, 'You have no permission')
        return redirect('library-home')

class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    permission_required = 'bookstore.change_book'
    
    model = Book
    context_object_name = 'book'
    fields = ['author','title', 'description']

    def handle_no_permission(self):
        messages.warning(self.request, 'You have no permission')
        return redirect('library-home')

class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):

    permission_required = 'bookstore.delete_book'
    
    model = Book
    context_object_name = 'book'


    def handle_no_permission(self):
        messages.warning(self.request, 'You have no permission')
        return redirect('library-home')