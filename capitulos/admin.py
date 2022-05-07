from django.contrib import admin
from .models import Capitulo
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class CapitulosAdmin(SummernoteModelAdmin):
    list_display = ('id','capitulo_titulo', 'capitulo_numero',
                    'capitulo_data', 'capitulo_publicado')
    list_display_links = ('id', 'capitulo_titulo', 'capitulo_numero')
    list_editable = ('capitulo_publicado',)


admin.site.register(Capitulo, CapitulosAdmin)