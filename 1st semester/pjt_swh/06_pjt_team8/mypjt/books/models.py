from django.db import models
from django.conf import settings

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.FloatField()
    author = models.CharField()

    def __str__(self):
        return f'{self.title} ({self.rating}/5.0)'
    
class Thread(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    read_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

