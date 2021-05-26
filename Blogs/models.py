from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)