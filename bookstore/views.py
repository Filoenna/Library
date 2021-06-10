from django.shortcuts import render
from django.http import HttpResponse

books = [
    {
        'author': 'Terry Pratchett',
        'title': 'Guards! Guards!',
        'description': 'Lorem ipsum simit dolor...',
        'year_published': '2012',
        'status': 'available'
    },
    {
        'author': 'Paolo Bacigalupi',
        'title': 'The Windup Girl',
        'description': 'Lorem ipsum simit dolor...',
        'year_published': '2010',
        'status': 'available'
    },
    {
        'author': 'Andrew Davidson',
        'title': 'The Gargoyle',
        'description': 'Lorem ipsum simit dolor...',
        'year_published': '2009',
        'status': 'available'
    },
    {
        'author': 'Hans Rosling',
        'title': 'Factfulness',
        'description': 'Lorem ipsum simit dolor...',
        'year_published': '2018',
        'status': 'available'
    },

]


def home(request):
    context = {
        'books': books
    }
    return render(request, 'bookstore/home.html', context)