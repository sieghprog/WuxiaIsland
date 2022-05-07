from django.contrib import admin
from .models import Novel
# Register your models here.

class NovelAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo_novel', 'autor_novel', 'categoria_novel', 'publicada_novel')
    list_display_links = ('titulo_novel',)
    list_editable = ('publicada_novel',)

admin.site.register(Novel, NovelAdmin)