from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'movie_pk': self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pk',)


class Review(models.Model):
    content = models.TextField()
    score = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)