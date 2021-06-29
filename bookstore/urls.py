from bookstore.models import Book
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, BookRentView, BookReturnView
from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='library-home'),
    path('book/<int:pk>/rent', views.BookRentView.as_view(), name='rent-book'),
    path('book/<int:pk>/return', views.BookReturnView.as_view(), name='return-book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
]
