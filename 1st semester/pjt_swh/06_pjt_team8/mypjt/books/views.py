from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Thread
from .forms import BookForm, ThreadForm

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
    thread_form = ThreadForm()
    threads = book.thread_set.all()
    context = {
        'book': book,
        'thread_form': thread_form,
        'threads': threads,
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

@login_required
def thread_create(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.book = book
            thread.save()
            print(thread)
            return redirect('books:thread_detail', thread.id)
        else:
            print('fail')
    else:
        form = ThreadForm()
    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'books/thread_create.html', context)


def thread_detail(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    context = {
        'thread' : thread
    }
    return render(request, 'books/thread_detail.html', context)


@login_required
def thread_update(request, thread_id):
    thread = Thread.objects.get(id=thread_id)

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect("books:thread_detail", thread.id)
    
    else:
        form = ThreadForm(instance=thread)
        
    context = {
        'form' : form,
        'thread' : thread,
    }
    return render(request, "books/thread_update.html", context)


@login_required
def thread_delete(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    id = thread.book.id
    thread.delete()
    return redirect("books:detail", id)
