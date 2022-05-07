from django.db import models
from novels.models import Novel
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=120)
    email_comentario = models.EmailField(verbose_name='Email')
    comentario = models.TextField()
    post_comentario = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name='Novel')
    usuario_comentario = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Usuário')
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return f'Comentário - {self.id}'
