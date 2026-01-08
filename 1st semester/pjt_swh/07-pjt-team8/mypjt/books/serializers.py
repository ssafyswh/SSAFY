from rest_framework import serializers
from .models import Book, Category, Thread, Comment


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ThreadListSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source='book.title', read_only=True)
    class Meta:
        model = Thread
        fields = ('id', 'title', 'book')


class ThreadSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source='book.title', read_only=True)
    
    class ThreadCommentsSerializer(serializers.ModelSerializer):
        thread = serializers.CharField(source='book.title', read_only=True)
        class Meta:
            model = Comment
            fields = '__all__'
    
    comments = ThreadCommentsSerializer(many=True, read_only=True)
    num_of_comments = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = '__all__'

    def get_num_of_comments(self, obj):
        return obj.comments.count()


class ThreadCreateSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source='book.title', read_only=True)
    class Meta:
        model = Thread
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'cover')


class BookSerializer(serializers.ModelSerializer):
    class BookThreadListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Thread
            fields = ('id', 'title', 'content','reading_date')

    category = CategoryListSerializer(read_only = True)

    threads = BookThreadListSerializer(many=True, read_only=True)

    num_of_threads = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_num_of_threads(self, obj):
        return obj.threads.count()
    

class CommentSerializer(serializers.ModelSerializer):
    thread = serializers.CharField(source='thread.title', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        