from apps.category.models import Category
from django.db import models
from apps.blog.models import Profile
from apps.comentary.models import Comentary


class Post(models.Model):
    STATUS_POST = [
        (True, 'Aproved'),
        (False, 'Not Aproved')
    ]

    owner = models.ForeignKey(Profile, 
    on_delete=models.SET_NULL, blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    text =  models.TextField()
    comentarys = models.ManyToManyField(Comentary, 
    blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(choices=STATUS_POST, default=True)
    
    @property
    def status_post(self):
        return self.status

    def post_valid(self, request):
        if self.owner == request.user.profile:
            self.title = request.POST['title']
            self.text = request.POST['text']
            self.save()
            response = {'status':'updated'}
        else:
            response = {'status':'You not owner of this post'}
        return response



    def __str__(self):
        return f'%s -> %s' % (self.owner , self.title)
   
    
    
