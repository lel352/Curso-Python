from django.db import models
# Create your models here.


class Categoria(models.Model):
    nome_cat = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):  # para aparecer o nome em vez de Categoria object
        return self.nome_cat