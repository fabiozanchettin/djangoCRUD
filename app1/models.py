from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
