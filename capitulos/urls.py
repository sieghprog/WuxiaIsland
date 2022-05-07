from django.urls import path
from . import views

urlpatterns = [
    path('novel/<int:pk>/<int:capitulo_numero')

]