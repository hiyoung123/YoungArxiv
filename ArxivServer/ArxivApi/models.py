from django.db import models

# Create your models here.

class PaperModel(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, default=0)
    pid = models.TextField()
    title = models.TextField()
    published = models.TextField()
    updated = models.TextField()
    summary = models.TextField()
    author = models.TextField()
    authors = models.TextField()
    cate = models.TextField()
    tags = models.TextField()
    link = models.TextField()
    pdf = models.TextField()
    version = models.TextField()