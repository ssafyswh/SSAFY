from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/index.html', context)

def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:index')
    else:
        form = BookForm()
    
    context = {
        'form': form
    }

    return render(request, 'books/create.html', context)

def detail(request, id):
    book = Book.objects.get(id=id)

    context = {
        'book': book,
    }

    return render(request, "books/detail.html", context)

def update(request, id):
    book = Book.objects.get(id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        
        book.title = title
        book.content = content
        book.author = author
        book.save()

        return redirect("books:detail", book.id)
    else:
        context = {
            'book': book,
        }
        return render(request, "books/update.html", context)


def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books:index')