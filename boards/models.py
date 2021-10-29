from django.db import models
# Create your models here.
class BlogPost(models.Model):
    username = models.CharField(max_length=150,default="")
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
