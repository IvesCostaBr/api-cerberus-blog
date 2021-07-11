from rest_framework import serializers
from .models import Comentary


class ComentarySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Comentary
        fields = ('owner', 'comment', 'date')
    

        
        