from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.



class Novel(models.Model):
    titulo_novel = models.CharField(max_length=120)
    autor_novel = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_novel = models.DateTimeField(default=timezone.now)
    descricao_novel = models.TextField()
    categoria_novel = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    imagem_novel = models.ImageField(upload_to='novel_img/%Y/%m')
    publicada_novel = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo_novel