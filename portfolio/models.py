from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
class Portfolio(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Images/portfolio')
    description=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} {self.created_date}"

class Category(models.Model):
    name=models.CharField(max_length=50)

class Comment(models.Model):
    full_name=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now=True)
    email=models.EmailField(max_length=100)
    message=models.TextField()

class Book(models.Model):
     title = models.CharField(max_length=255)
     author = models.CharField(max_length=255)
     cover_image = models.ImageField(upload_to='book_cover/')
     spine_image = models.ImageField(upload_to='book_spine/')
     publisher = models.CharField(max_length=255)
     publication_date = models.DateField()
     pages = models.IntegerField()
     description = models.CharField(max_length=100)
     def __str__(self):
        return f"{self.title} {self.author} "
    
class Gallery(models.Model):
    image=models.ImageField(upload_to='Images/Gallery')
    title=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} "
class Blog(models.Model):
    image=models.ImageField(upload_to='Images/blog')
    title=models.CharField(max_length=50)
    created_date=models.DateTimeField(auto_now=True)
    description = models.TextField()
    
class About(models.Model):
    image=models.ImageField(upload_to='Images/about')
    title=models.CharField(max_length=70)
    description=models.TextField()