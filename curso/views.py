from django.shortcuts import render, redirect
from .models import curso
from .forms import CursoForm

# Vista para listar los cursos
def get_curso(request):
    curso_id = request.GET.get('curso')  
    cursos = curso.objects.all()  

    if curso_id:
        cursos_filtrados = cursos.filter(id=curso_id)  
    else:
        cursos_filtrados = cursos  

    return render(request, 'lista-curso.html', {
        'title': 'Lista de cursos',
        'cursos': cursos,  
        'cursos_filtrados': cursos_filtrados,  
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

    return render(request, 'formulario-curso.html', {'form': form})
