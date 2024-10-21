# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=255) 
#     author = models.CharField(max_length=255)  
#     published_date = models.DateField() 

#     def __str__(self):
#         return self.title



from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author) 
    publishers = models.ManyToManyField(Publisher)
    published_date = models.DateField()
    details = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return self.title

