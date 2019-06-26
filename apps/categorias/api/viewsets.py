from rest_framework.viewsets import ModelViewSet
from apps.categorias.models import Categoria
from apps.categorias.api.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
