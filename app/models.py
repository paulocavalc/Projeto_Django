from django.contrib.auth.models import User
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=50)


class Postagem(models.Model):
    titulo = models.CharField(max_length=250)
    conteudo = models.TextField()
    autor = models.ForeignKey(to=User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Postagens"