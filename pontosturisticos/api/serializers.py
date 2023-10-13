from rest_framework.serializers import ModelSerializer

from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from pontosturisticos.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    endereco = EnderecoSerializer()
    class Meta:
        model = PontoTuristico
        fields = '__all__'
        # fields = ('nome', 'descricao', 'aprovado',
        #           'atracoes','comentarios','avaliacoes',
        #           'endereco')