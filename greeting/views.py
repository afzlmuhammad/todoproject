from django.shortcuts import render
from .forms import BookForm
from .models import Book

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return render(request, 'form-data.html', {
                'message': 'Book details saved successfully'
                
            })
    else:
        form = BookForm()
        
    return render(request, 'index.html', {'form': form})


def all_books(request):
    books = Book.objects.all()
    return render(request, 'all-books.html', {'books': books})
