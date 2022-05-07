from django.contrib import admin
from .models import Capitulo
# Register your models here.
class CapituloAdmin(admin.ModelAdmin):
    list_display = ('id','capitulo_titulo', 'capitulo_numero', 'capitulo_data', 'capitulo_publicado')
    list_display_links = ('id','capitulo_titulo', 'capitulo_numero')
    list_editable = 'capitulo_publicado'


admin.site.register(Capitulo, CapituloAdmin)