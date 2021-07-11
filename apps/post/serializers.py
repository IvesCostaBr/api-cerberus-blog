from rest_framework import serializers
from .models import Post
from apps.comentary.models import Comentary
from apps.comentary.serializers import ComentarySerializer



class PostSerializer(serializers.ModelSerializer):
    comentarys = ComentarySerializer(many=True)
    class Meta:
        model = Post
        fields = (
            'id', 
            'owner',
            'date_creation',
            'title',
            'text',
            'comentarys',
            'category'
        )
        read_only_fields = ['category',]

    def create_comments(self, post, comentarys):
        for comentary in comentarys:
            co = Comentary.objects.create(**comentary)
            post.comentarys.add(co)
            

    def create(self, validated_data):
        comentarys = validated_data['comentarys']
        del validated_data['comentarys']
        post = Post.objects.create(**validated_data)
        self.create_comments(post, comentarys)
        
        return post
    
    # def partial_update(self, validated_data):
    #     print('Aqui')
        
    def update(self, instance, validated_data):
        comentarys = validated_data['comentarys']
        del validated_data['comentarys']
        self.create_comments(instance, comentarys)
        return instance

        

        