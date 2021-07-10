from django.db import models
from apps.post.models import Post

class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    img = models.ImageField(upload_to='img', blank=True, null=True)
    posts = models.ManyToManyField(Post, blank=True)
