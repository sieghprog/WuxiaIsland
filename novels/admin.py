from django.contrib import admin
from .models import Novel
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class NovelAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo_novel', 'autor_novel', 'status_novel', 'publicada_novel')
    list_display_links = ('titulo_novel',)
    list_editable = ('publicada_novel',)

admin.site.register(Novel, NovelAdmin)