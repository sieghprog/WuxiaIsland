from django.db import models
from django.utils import timezone
from novels.models import Novel
# Create your models here.


class Capitulo(models.Model):
    capitulo_novel = models.ForeignKey(Novel, on_delete=models.DO_NOTHING, verbose_name='Novel')
    capitulo_numero = models.IntegerField(verbose_name='Número', blank=True, null=True)
    capitulo_titulo = models.CharField(max_length=90, verbose_name='Título')
    capitulo_texto = models.TextField(verbose_name='Texto')
    capitulo_data = models.DateTimeField(default=timezone.now, verbose_name='Data')
    capitulo_publicado = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return f'{self.capitulo_numero} - {self.capitulo_titulo}'

    class Meta:
        ordering = ['capitulo_numero']
