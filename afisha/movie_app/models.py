from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = 'Директор'
        verbose_name_plural = 'Директоры'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__ (self):
        return f"{self.title} ({self.director.name})"

STARS = [(i, str(i)) for i in range(1, 6)]
class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    star = models.IntegerField(choices=STARS, default=5)

    def __str__ (self):
        return f"Review for {self.movie.title}"

