from rest_framework import (
    viewsets,
    permissions, 
    authentication,
    response,
    decorators as rest_decoratos 
    )
from django.core import serializers
from .serializers import PostSerializer
from .models import Post
import logging

logger = logging.getLogger('django')


class PostManagerViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get', 'post', 'patch', 'delete']
    

    def get_queryset(self):
        return Post.objects.all()
    
    def create(self, request, *args, **kwargs):
        user_request = request.user
        self.kwargs['user'] = user_request
        return super(PostManagerViewSet, self).create(request, *args, **kwargs)
        
        # # post = Post.objects.create(
        # #     owner=self.request.user.profile,
        # #     title=request.data['title'],
        # #     text=request.data['text']
        # # )

        # return response.Response(model_to_dict(post))
    
    # def partial_update(self,request, *args, **kwargs):
    #     # post = self.get_object()
    #     # response = post.post_valid(request)
    #     # return response.Response(response)
    #     return super(PostManagerViewSet, self).partial_update(request, *args, **kwargs)
        
    def update(self, request, *args, **kwargs):
        return super(PostManagerViewSet, self).update(request, *args,)

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
        
        return response.Response(response)

    @rest_decoratos.action(methods=['GET'],detail=False)
    def delete_all_posts(self, request):
        if self.request.user.is_authenticated:
            Post.objects.all().delete()
            resp = {'STATUS':'OK'}
        else:
            resp = {'STATUS':'You dont have permission for run tihs action'}
        
        return response.Response(resp)


@rest_decoratos.api_view(['GET'])
def list_post(request):
    list = Post.objects.all()[:10]
    list = list.values()
    return response.Response(list)

@rest_decoratos.api_view(['GET'])
def detail_post(request, id): 
    print(request.user) 
    json_response = PostSerializer(Post.objects.get(id=id)).data
    return response.Response(json_response)
    






