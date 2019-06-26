from rest_framework.viewsets import ModelViewSet
from apps.produtos.models import Produto
from apps.produtos.api.serializers import ProdutoSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
