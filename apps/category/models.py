from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    img = models.ImageField(upload_to='category_img', blank=True, null=True)

    def __str__(self):
        return self.name
