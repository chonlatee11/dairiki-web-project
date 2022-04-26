import email
from turtle import title
from unicodedata import name
from django.db import models
# Create your models here.

class ContactMessage(models.Model) :
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    detail = models.TextField(blank=False,null=False)
    
    def __str__(self):
        return self.subject