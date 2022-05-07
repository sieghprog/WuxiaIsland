from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

# Create your views here.
class NovelIndex(ListView):
    pass

class NovelBusca(NovelIndex):
    pass

class NovelCategoria(NovelIndex):
    pass

class NovelDetalhes(NovelIndex):
    pass