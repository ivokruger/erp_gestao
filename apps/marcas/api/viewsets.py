from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from apps.marcas.models import Marca
from apps.marcas.api.serializers import MarcaSerializer

class MarcaViewSet(ModelViewSet):
#    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    def get_queryset(self):
        return Marca.objects.filter(ativo=True)

#    def list(self, request, *args, **kwargs):
#        return Response({'teste': 123})

#    def create(self, request, *args, **kwargs):
#        return Response({'Hello': request.data['nome']})

#    def destroy(self, request, *args, **kwargs):
#        pass

#    def retrieve(self, request, *args, **kwargs):
#        pass

#    def update(self, request, *args, **kwargs):
#        pass

#    def partial_update(self, request, *args, **kwargs):
#        pass

#   Aula 6. Implementando suas próprias actions personalizadas

    @action(methods=['post', 'get'], detail=True)
    def minha_action(self,request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self,request):
        pass

