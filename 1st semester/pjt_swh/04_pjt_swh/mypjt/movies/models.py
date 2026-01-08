from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    story = models.TextField()
    director = models.TextField()
