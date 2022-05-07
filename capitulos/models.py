from django.db import models
from django.utils import timezone
# Create your models here.

class Capitulo(models.Model):
    capitulo_numero = models.IntegerField('')
    capitulo_titulo = models.CharField('')
    capitulo_texto = models.TextField('')
    capitulo_data = models.DateTimeField(default=timezone.now)
    capitulo_publicado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.capitulo_numero} - {self.capitulo_titulo}'