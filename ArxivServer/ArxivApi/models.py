from django.db import models

# Create your models here.

class PaperModel(models.Model):
    # id = models.IntegerField(primary_key=True)
    pid = models.TextField()
    title = models.TextField()
    published = models.TextField()
    updated = models.TextField()
    summary = models.TextField()
