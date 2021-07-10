from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from apps.blog import viewsets as app_blog
from apps.post import viewsets as app_post

router = routers.DefaultRouter()
router.register(r'profiles', app_blog.ProfileViewSet, basename='Profile')
router.register(r'users', app_blog.UserViewSet, basename='User')
router.register(r'posts', app_post.PostViewSet, basename='Post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token)
]
