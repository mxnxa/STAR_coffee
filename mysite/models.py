from django.db import models

# Create your models here.
class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)
    pub_date = models.DateTimeField('date published')