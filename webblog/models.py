from typing import Any
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class ContactTb(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    phone=models.IntegerField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}-{self.email}"

class Popular_Blog(models.Model):
    title =models.CharField(max_length=122)
    author = models.CharField(max_length=50)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    images=models.ImageField(default="")
    def __str__(self):
        # return f"{self.title}"
        return self.title
    
    
class Regular_Blog(models.Model):
    title =models.CharField(max_length=122)
    author = models.CharField(max_length=50)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    images=models.ImageField(default="")
    