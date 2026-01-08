from django import forms
from .models import Book, Thread

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        labels = {
            'title': '도서명',
            'content': '설명',
            'rating': '평점',
            'author': '저자',
        }
        fields = '__all__'

        help_texts = {
            'rating': '0.0에서 5.0 사이의 평점을 입력하세요.',
        }
        error_messages = {
            'title': {
                'required': '도서 제목은 필수 항목입니다.',
            },
            'rating': {
                'invalid': '올바른 숫자 값을 입력하세요.',
            }
        }

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        labels = {
            'title': '제목',
            'content': '내용',
            'read_at': '독서일',
            'created_at': '작성일',
            'updated_at': '마지막 수정',
        }
        fields = ('title', 'content', 'read_at',)
        widgets = {
            'read_at': forms.DateInput(attrs={'type': 'date'})
        }