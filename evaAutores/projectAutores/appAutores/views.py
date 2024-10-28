from django.shortcuts import render
from appAutores.models import Autor
from appAutores.forms import FormAutor

# Create your views here.
def listaAutores(request):
    autores = Autor.objects.all()
    data = {'autores': autores}
    return render(request, 'appAutores/index.html', data)