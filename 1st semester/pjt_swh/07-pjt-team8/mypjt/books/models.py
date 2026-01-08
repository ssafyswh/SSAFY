from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

# Create your models here.


class Book(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    isbn = models.CharField(max_length=20)
    cover = models.TextField()
    publisher = models.TextField()
    pub_date = models.DateField()
    author = models.CharField()
    customer_review_rank = models.IntegerField(
        validators=[
            MinValueValidator(0),  # 최솟값 0
            MaxValueValidator(10)  # 최댓값 10
        ]
    )

    def __str__(self):
        return f'{self.title} ({self.customer_review_rank}/5.0)'
    
class Thread(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='threads')
    title = models.CharField(max_length=50)
    content = models.TextField()
    reading_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=20)


class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)