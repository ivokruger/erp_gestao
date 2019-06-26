from django.db import models

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.TextField('Descricao Da Marca', max_length=30, blank=True)
    ativo = models.BooleanField(default=True)
    data_registro = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'marcas'
        ordering = ('descricao',)
