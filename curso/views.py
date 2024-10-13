from django.shortcuts import render, redirect
from .models import curso
from .forms import CursoForm

# Vista para listar los cursos
def get_curso(request):
    cursos = curso.objects.all()
    return render(request, 'lista-curso.html', {
        'title': 'Lista de cursos',
        'cursos': cursos,
    })

# Vista para agregar o editar cursos
def formulario(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo curso
            return redirect('lista-cursos')  # Redirige a la página de lista de cursos después de guardar
    else:
        form = CursoForm()

    return render(request, 'formulario_curso.html', {'form': form})
