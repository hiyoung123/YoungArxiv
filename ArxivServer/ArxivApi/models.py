from django.db import models

# Create your models here.

class PaperModel(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.TextField()
    title = models.TextField()
    published = models.DateTimeField()
    updated = models.DateTimeField()
    summary = models.TextField()
    author = models.TextField()
    authors = models.TextField()
    cate = models.TextField()
    tags = models.TextField()
    link = models.TextField()
    pdf = models.TextField()
    version = models.TextField()
    favorite = models.IntegerField()
    pv = models.IntegerField()
    pv_total_times = models.TimeField()

    class Index:
        name = 'Papers'