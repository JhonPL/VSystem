from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm

def get_cursos(request):
    cursos = Curso.objects.all()   
    return render(request, 'lista-curso.html', {
        'title': 'Lista de cursos',
        'cursos': cursos
        })
    
def formulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo curso
            return redirect('lista-cursos')  # Redirige a la página de lista de cursos después de guardar
    else:
        form = CursoForm()

    return render(request, 'formulario_curso.html', {'form': form})