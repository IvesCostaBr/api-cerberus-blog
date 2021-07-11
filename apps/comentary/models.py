from django.db import models
from apps.blog.models import Profile


class Comentary(models.Model):
    STATUS = [
        (True, 'Aproved'),
        (False, 'Not Aproved')
    ]

    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    head = models.CharField(max_length=40)
    txt = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True, choices=STATUS)


    def __str__(self):
        return f'%s -> %s' % (str(self.owner) ,str(self.head)) 