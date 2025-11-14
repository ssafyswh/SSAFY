from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Book, Thread, Category, Comment
from .serializers import CategoryListSerializer, BookListSerializer, BookSerializer, ThreadListSerializer, ThreadSerializer, ThreadCreateSerializer, CommentSerializer

'''
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
'''

@api_view(['GET'])
def book_list(reqeust):
    books = get_list_or_404(Book)
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def book_detail(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)


@api_view(['GET'])
def category_list(request):
    categories = get_list_or_404(Category)
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def thread_list(request):
    threads = get_list_or_404(Thread)
    serializer = ThreadListSerializer(threads, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def thread_detail(request, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)
    if request.method == 'GET':
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(thread=thread)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        serializer = ThreadSerializer(thread, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_thread(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == 'POST':
        serializer = ThreadCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])    
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)