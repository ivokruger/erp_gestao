from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from apps.produtos.models import Produto
from apps.marcas.api.serializers import MarcaSerializer
from apps.categorias.api.serializers import CategoriaSerializer

class ProdutoSerializer(ModelSerializer):

    marca = MarcaSerializer()
    categoria = CategoriaSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = Produto
        fields = (
            'id',
            'marca',
            'categoria',
            'descricao',
            'descricao_completa',
            'descricao_completa2',
        )

    def get_descricao_completa(self, obj):
#       return '%s - %s' % (obj.id, obj.descricao)
        return (str(obj.id) + ' = ' + obj.descricao)

