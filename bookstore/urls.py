from bookstore.models import Book
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from . import views

urlpatterns = [
    path('', BookListView.as_view(), name='library-home'),
    path('book/<int:new_pk>/rent', views.rent, name='rent-book'),
    path('book/<int:new_pk>/return', views.breturn, name='return-book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
]
