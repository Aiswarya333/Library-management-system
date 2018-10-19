from __future__ import unicode_literals
from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=230)
    published_date = models.DateField(blank=False, null=False)
    availability=models.CharField(max_length=10)

    def __str__(self):
        return self.title



class User(models.Model):
    user_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_name = models.CharField(max_length=100, unique =True)
    password = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
