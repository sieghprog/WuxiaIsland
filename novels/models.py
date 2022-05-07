from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Novel(models.Model):
    titulo_novel = models.CharField(max_length=120)
    autor_novel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    data_novel = models.DateTimeField(default=timezone.now)
    descricao_novel = models.TextField()
    categoria_novel = models.ManyToManyField(Categoria, verbose_name='Categoria')
    imagem_novel = models.ImageField(upload_to='novel_img/%Y/%m')
    publicada_novel = models.BooleanField(default=False)
    class Status(models.TextChoices):
        COMPLETE = 'Complete', _('Complete')
        ONGOING = 'Ongoing', _('Ongoing')

    status_novel = models.CharField(
        max_length = 8,
        choices = Status.choices,
        default = Status.ONGOING,
    )

    def __str__(self):
        return self.titulo_novel