from django.db import models

class ordem(models.Model):
    id_ordem = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    responsavel = models.TextField(max_length=255)

