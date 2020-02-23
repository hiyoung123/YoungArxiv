from django.db import models

# Create your models here.

class PaperModel(models.Model):
    id = models.AutoField(primary_key=True)
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

    class Index:
        name = 'Papers'