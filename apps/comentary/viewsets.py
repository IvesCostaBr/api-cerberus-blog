from rest_framework import viewsets
from .models import Comentary
from .serializers import ComentarySerializer


class ComentaryViewSet(viewsets.ModelViewSet):
    serializer_class = ComentarySerializer


    def get_queryset(self):
        return Comentary.objects.all()

    