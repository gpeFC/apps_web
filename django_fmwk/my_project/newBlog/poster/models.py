from django.db import models

# Modelos para la app Poster (Project: newBLog)

class Category(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category)
    creation_date = models.DateTimeField(auto_now_add=True)
