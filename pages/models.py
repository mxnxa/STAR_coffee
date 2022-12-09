from django.db import models

# Create your models here.
class History(models.Model):
    year = models.IntegerField(default=2010)
    content = models.TextField()