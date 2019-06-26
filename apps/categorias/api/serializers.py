from rest_framework.serializers import  ModelSerializer
from apps.categorias.models import Categoria

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id',
            'estrutura',
            'descricao',
            'ativo')
