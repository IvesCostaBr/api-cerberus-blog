from django.contrib.auth.models import User
from rest_framework import viewsets, response, permissions, authentication, decorators
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    
    def get_queryset(self):
        return Profile.objects.all()

    def create(self,request, *args, **kwargs):
        return super(ProfileViewSet, self).create(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
   
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    # authentication_classes = (authentication.TokenAuthentication,)

    def get_queryset(self):
        return User.objects.all()
    
    def create(self, request, *args, **kwargs):
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return response.Response({'status':'CREATED'})

  
    def partial_update(self,request, *args, **kwargs):
        print('Entrei no path')

    @decorators.action(['GET'], detail=False)
    def delete_all(self, request):
        User.objects.all().delete()
        return response.Response({'status':'ALL DELETED'})


    



