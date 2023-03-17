from django.shortcuts import render
from fotos_index.models import Fotos

def index(request):
   fotos = Fotos.objects.order_by('titulo')
   contexto = { 'fotos' : fotos}
   
   return render(request, 'index.html', contexto)