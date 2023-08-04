from rest_framework.serializers import ModelSerializer

from pontosturisticos.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = '__all__'