from django.db import models

# Create your models here.
class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image = models.ImageField(upload_to='static/files/', blank=True, null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title