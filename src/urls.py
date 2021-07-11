from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from apps.blog import viewsets as app_blog
from apps.post import viewsets as app_post
from apps.comentary import viewsets as app_comentary
from apps.category import viewsets as app_category

router = routers.DefaultRouter()
router.register(r'profiles', app_blog.ProfileViewSet, basename='Profile')
router.register(r'users', app_blog.UserViewSet, basename='User')
router.register(r'posts', app_post.PostManagerViewSet, basename='Post')
router.register(r'comentarys', app_comentary.ComentaryViewSet, basename='Comentary')
router.register(r'categorys-admin', app_category.CategoryAdminViewSet, basename='Category')


urlpatterns = [
    path('super/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token),
    path('list_post/', app_post.list_post),
    

]
