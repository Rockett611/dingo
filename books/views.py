from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from books.models import Book, Author


def book_list(request):
    books = Book.objects.all()
    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'books': books})

def book_details(request, id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=book.author_id)
    return render(request, 'books/book_detail.html', {'book': book, 'author': author})


def author_list(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 5)
    page_number = request.GET.get('page')
    authors = paginator.get_page(page_number)
    return render(request, 'books/author_list.html', {'authors': authors})


def author_details(request, id):
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author_id=id)
    return render(request, 'books/author_details.html', {'author': author, "books": books})
