from django.db import models

# Create your models here.
class post(models.Model):
    imageurl  = models.TextField()
    description = models.TextField()
    title = models.TextField()
    author = models.TextField()