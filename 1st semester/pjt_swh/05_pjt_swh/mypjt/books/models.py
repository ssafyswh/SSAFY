from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    content = models.TextField()
    rating = models.FloatField()
    author = models.CharField()

    def __str__(self):
        return f'{self.title} ({self.rating}/5.0)'