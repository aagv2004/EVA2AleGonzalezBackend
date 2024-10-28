from django.shortcuts import render, redirect
from appAutores.models import Autor
from appAutores.forms import FormAutor

# Create your views here.
def listaAutores(request):
    autores = Autor.objects.all()
    data = {'autores': autores}
    return render(request, 'appAutores/autores.html', data)

def agregarAutores(request):
    form = FormAutor()
    if request.method == "POST":
        form = FormAutor(request.POST)
        if form.is_valid():
            form.save()
        return listaAutores(request)
    data = {'form':form}
    return render(request, 'appAutores/agregarAutores.html', data)

def actualizarAutores(request, id):
    autores = Autor.objects.get(id=id)
    form = FormAutor(instance=autores)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        return listaAutores(request)
    data = {'form':form}
    return render(request, 'appAutores/agregarAutores.html', data)

def eliminarAutores(request, id):
    autores = Autor.objects.get(id = id)
    autores.delete()
    return redirect(listaAutores)