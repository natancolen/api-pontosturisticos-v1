from rest_framework.serializers import ModelSerializer

from comentarios.models import Comentario

class ComentarioSerializer(ModelSerializer):

    class Meta:
        model = Comentario
        field = '__all__'