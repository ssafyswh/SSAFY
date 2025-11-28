from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (
    require_http_methods,
    require_safe,
    require_POST,
)
from django.contrib.auth.decorators import login_required

from accounts.models import Category
from .models import Book, Thread, Comment
from .forms import ThreadForm, CommentForm
from .utils import (
    generate_image_with_openai,
)


# Index 페이지
def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    context = {
        'books': books,
        'categories': categories
    }
    return render(request, "books/index.html", context)

# 장르별 필터링
def filter_category(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        if category_id and category_id.isdigit() and int(category_id) > 0:
            filtered_book = Book.objects.filter(category_id=category_id)
        else:
            filtered_book = Book.objects.all()

        book_list = []
        for book in filtered_book:
            category_name = book.category.name if book.category else ''
            sub_title = getattr(book, 'subTitle', '')
            book_list.append({
                'id': book.id,
                'title': book.title,
                'sub_title': sub_title,
                'author': book.author,
                'cover': book.cover,
                'category_name': category_name,
            })

        return JsonResponse({'books': book_list})
    return JsonResponse({'error': 'Invalid request method'}, status=400)
    

@require_safe
def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    context = {
        "book": book,
    }
    return render(request, "books/detail.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def thread_create(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == "POST":
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.book = book
            thread.user = request.user
            thread.save()

            generated_image_path = generate_image_with_openai(thread.title, thread.content, book.title, book.author)
            if generated_image_path:
                thread.cover_img = generated_image_path
                thread.save()
                
            return redirect("books:thread_detail", book.pk, thread.pk)
    else:
        form = ThreadForm()
    context = {
        "form": form,
        "book": book,
    }
    return render(request, "books/thread_create.html", context)


@login_required
@require_safe
def thread_detail(request, book_pk, thread_pk):
    book = Book.objects.get(pk=book_pk)
    thread = Thread.objects.get(pk=thread_pk)
    comment_form = CommentForm()
    context = {
        "book" : book,
        "thread": thread,
        "comment_form" : comment_form,
    }
    return render(request, "books/thread_detail.html", context)



@login_required
@require_http_methods(["GET", "POST"])
def thread_update(request, book_pk, thread_pk):
    book = Book.objects.get(pk=book_pk)
    thread = Thread.objects.get(pk=thread_pk)
    comment_form = CommentForm(request.POST)
    if thread.user == request.user:
        if request.method == "POST":
            form = ThreadForm(request.POST, request.FILES, instance=thread)
            if form.is_valid():
                form.save()  
                return redirect('books:thread_detail', book_pk=book.pk, thread_pk=thread.pk)
        else:
            form = ThreadForm(instance=thread)
    else :
        return redirect('books:index') 
    context = {
        "form": form,
        "book": book,
        "comment_form" : comment_form,
    }
    return render(request, "books/thread_update.html", context)


@login_required
@require_POST
def thread_delete(request, book_pk, thread_pk):
    thread = Thread.objects.get(pk=thread_pk)
    if thread.user == request.user:
        thread.delete()
    return redirect("books:detail", book_pk)


# 쓰레드 좋아요 비동기 처리
def likes(request, book_pk, thread_pk):
    # Thread 객체 가져오기
    thread = get_object_or_404(Thread, pk=thread_pk)
    # 좋아요 로직: 이미 좋아요를 눌렀다면 취소, 아니면 추가
    if thread.likes.filter(pk=request.user.pk).exists():
        thread.likes.remove(request.user)
        is_liked = False
    else:
        thread.likes.add(request.user)
        is_liked = True
    
    # 클라이언트에 보낼 데이터
    context = {
        'is_liked': is_liked,
        'likes_count': thread.likes.count(),
    }
    return JsonResponse(context)

# 쓰레드 댓글 비동기 처리
@require_POST
@login_required
def create_comment(request, book_pk, thread_pk):
    content = request.POST.get('content')
    thread = get_object_or_404(Thread, pk=thread_pk)

    comment = Comment.objects.create(
        content=content,
        thread=thread,
        user=request.user
    )

    comment.save()
    context = {
        'content': comment.content,
        'userName': comment.user.username,
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M'),
        'commentPk': comment.pk,
    }
    
    return JsonResponse(context)

@require_POST
def delete_comment(request, book_pk, comment_pk):
    if request.user.is_authenticated:
        # 댓글 가져오기 (없으면 404)
        comment = get_object_or_404(Comment, pk=comment_pk)
        
        # 작성자 본인인지 확인
        if request.user == comment.user:
            comment.delete()
            return JsonResponse({'status': 'ok'})
            
    # 권한이 없거나 실패 시
    return JsonResponse({'status': 'fail'}, status=403)