from rest_framework.response import Response
from rest_framework import viewsets, permissions, authentication
from .serializers import PostSerializer
from .models import Post
import logging

logger = logging.getLogger('django')


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'post', 'patch', 'delete']
    

    def get_queryset(self):
        return Post.objects.all()
    
    def create(self, request, *args, **kwargs):
        Post.objects.create(
            owner=self.request.user.profile,
            title=request.POST['title'],
            text=request.POST['text']
        )
        return Response({'STATUS':201})
    
    def partial_update(self,request, *args, **kwargs):
        post = self.get_object()
        response = post.post_valid(request)
        return Response(response)
        

    def destroy(self,request, *args, **kwargs):
        try:
            post = Post.objects.get(pk=kwargs['pk'])
        except Exception:
            response = {'STATUS':'Register not found'}
        if request.user.profile == post.owner:
            post.delete()
            response = {'STATUS':'DELETED'}
        else:
            response = {'STATUS':'you does not owner of this post'}
        
        return Response(response)
