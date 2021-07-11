from rest_framework import serializers
from .models import Category
from apps.post.serializers import PostSerializer


class CategorySerializer(serializers.ModelSerializer):
    post_set = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('name', 'description', 'img', 'post_set')
        read_only_fields = ['img', 'post_set', ]