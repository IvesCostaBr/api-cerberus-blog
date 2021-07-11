from rest_framework import (
    viewsets, 
    permissions, 
    authentication,
    response,
    decorators as rest_api
)
from .serializers import CategorySerializer
from .models import Category
from django.shortcuts import render

class CategoryAdminViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (authentication.TokenAuthentication, )
    permission_classes = (permissions.IsAdminUser,)
    
    def get_queryset(self):
        return Category.objects.all()

    @rest_api.action(methods=['GET'], detail=False)
    def category_list(self, request):
        return response.Response({})


@rest_api.api_view(['GET'])
@rest_api.schema(None)
def get_categorys(request):
    list_categorys = Category.objects.all()
    list = list_categorys.values()
    return response.Response(list)




    




    

    