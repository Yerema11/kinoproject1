from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=255)
    session_time = models.DateTimeField()
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Билет на {self.movie_name} - {self.seat_number}"


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Post(models.Model):  # Пост должен быть отдельной моделью
    POST_TYPES = [
        ('movie', 'Movie'),
        ('news', 'News'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.title
