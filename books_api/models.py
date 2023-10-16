from django.db import models

class Books(models.Model):
    """Modelo de Livros"""

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    isVendido = models.BooleanField(default=False)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        """Retorna o nome do livro."""
        return self.nome
