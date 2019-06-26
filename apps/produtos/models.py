from django.db import models
from apps.marcas.models import Marca
from apps.categorias.models import Categoria

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100, blank=False, unique=False, null=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'produtos'

    @property
    def descricao_completa2(self):
        return '%s - %s' % (str(self.id), self.descricao)
#        return (str(self.id) + ' = ' + self.descricao)

