from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

# --- Read ---


def index(request):
    """전체 게시글 목록을 조회하여 index.html 페이지를 렌더링"""
    # 1. Article 모델을 통해 DB에 저장된 모든 데이터를 조회
    articles = Article.objects.all()

    # 2. 조회된 데이터를 템플릿에 전달하기 위해 context 딕셔너리에 담음
    #    템플릿에서는 'articles'라는 키로 QuerySet 객체에 접근할 수 있음
    context = {
        'articles': articles,
    }
    # 3. request, 템플릿 경로, context를 render 함수에 전달하여 최종 HTML을 생성하고 사용자에게 응답
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    """특정 pk(Primary Key)를 가진 게시글 하나를 조회하여 detail.html 페이지를 렌더링"""
    # 1. URL로부터 전달받은 pk 값을 사용하여, 해당 pk를 가진 Article 객체 하나를 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회된 단일 게시글 객체를 context에 담아 템플릿에 전달
    context = {
        'article': article,
    }
    # 3. detail.html 템플릿을 렌더링
    return render(request, 'articles/detail.html', context)


# --- Create ---

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
 


# --- Delete ---


def delete(request, pk):
    """특정 pk를 가진 게시글을 DB에서 삭제"""
    # 1. 삭제할 게시글을 pk를 이용해 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회된 객체의 .delete() 메서드를 호출하여, DB에서 해당 레코드를 삭제(DELETE)
    article.delete()

    # 3. 게시글 삭제 후, 전체 목록 페이지로 이동
    return redirect('articles:index')


# --- Update ---


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
