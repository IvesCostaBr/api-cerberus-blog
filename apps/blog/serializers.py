from django.contrib.auth.models import User
from .models import Profile
from rest_framework import serializers
from apps.post import serializers as serializer_post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    post_set = serializer_post.PostSerializer(many=True)
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('nickname', 'description', 'user', 'post_set')
