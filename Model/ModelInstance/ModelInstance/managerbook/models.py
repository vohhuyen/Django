from django.db import models
from datetime import date
from datetime import datetime

class Author(models.Model):
    name = models.CharField(max_length=255)
    birthdate = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    rating = models.FloatField()

    def __str__(self):
        return f"{self.title} - {self.author.name}"

    def is_valid(self):
        return all([self.title, self.author, self.published_date, self.isbn, self.pages, self.rating])

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('book_detail', kwargs={'pk': self.pk})
    def get_book_summary(self):
        return f"{self.title} by {self.author.name}, {self.published_date.year}"

