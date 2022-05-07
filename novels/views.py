from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from novels.models import Novel
# Create your views here.
class NovelIndex(ListView):
    model = Novel
    template_name = 'novels/index.html'
    paginate_by = 3
    context_object_name = 'novels'

class NovelBusca(NovelIndex):
    pass

class NovelCategoria(NovelIndex):
    pass

class NovelDetalhes(NovelIndex):
    pass