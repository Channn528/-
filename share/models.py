from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
from django.db import models
from django import forms
from django.utils import timezone

# Create your models here.
class Content(models.Model):
     image = models.ImageField(upload_to='images/')
     title = models.CharField(max_length=200)

     content = models.TextField()

     created_at = models.DateTimeField(auto_now_add = True)
     updated_at = models.DateTimeField(auto_now = True)
     
     def __str__(self):
          return self.title
     

class Comment(models.Model):
     comment = models.TextField()
     content = models.ForeignKey(Content, on_delete=models.CASCADE)