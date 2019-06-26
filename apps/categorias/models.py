from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    estrutura = models.CharField('Chave De Estrutura', max_length=50, blank=False, unique=True)
    descricao = models.TextField('Descricao Da Categogia', max_length=100, blank=True)
    ativo = models.BooleanField(default=False)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'categorias'
        ordering = ('estrutura',)
