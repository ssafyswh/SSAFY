from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer


# DRF의 모든 뷰 함수는 반드시 api_view 데코레이터가 필수.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 전체 게시글 데이터 조회
        articles = Article.objects.all()
        # Serialization 진행
        serializer = ArticleListSerializer(articles, many=True)
        # serializer 덩어리에서 데이터 추출 (.data 속성)한 것을 응답
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # 예전 코드
        # form = ArticleForm(request.POST)
        # 1. 사용자가 보낸 입력 데이터를 직렬화
        serializer = ArticleSerializer(data=request.data)
        # 2. 직렬화된 데이터를 유효성 검사
        if serializer.is_valid():
            # 3. 저장
            serializer.save()
            # 4. 저장이 성공했다는 응답 (201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 5. 저장이 실패했다는 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PATCH'])
def article_detail(request, article_pk):
    # 단일 게시글 조회
    article = Article.objects.annotate(num_of_comments=Count('comment')).get(pk=article_pk)
    if request.method == 'GET':
        # 조회 한 결과를 직렬화
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        # 과거 코드
        # form = ArticleForm(request.POST, instance=article)
        # 1. 사용자로부터 새로운 입력 데이터를 받아 직렬화 진행(+ 기존 데이터)
        # serializer = ArticleSerializer(article, data=request.data)
        # 데이터 일부만 수정하려면 partial=True를 설정해야 함
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # serializer = ArticleSerializer(instance=article, data=request.data)
        # 2. 직렬화 결과를 유효성 검사
        if serializer.is_valid():
            serializer.save()
            # 3. 수정이 성공했다는 응답
            return Response(serializer.data)
        # 4. 수정이 실패했다는 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == "GET":
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == "DELETE":
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
