import uuid
from django.db import models

class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(default="example@example.com")

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ['last_name']  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Musician(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['last_name']), 
        ]
        verbose_name = "Musician"
        verbose_name_plural = "Musicians"
        ordering = ['last_name', 'first_name'] 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField(default=0) 

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ['release_date'] 
        unique_together = (('artist', 'name'),) 

    def __str__(self):
        return self.name


