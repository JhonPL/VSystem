from django.shortcuts import render, redirect
from .models import EstudianteCurso
from .forms import EstudianteCursoForm

# Vista para listar los estudiantes y cursos
def Estudiante_Curso(request):
     # Obtener los valores del filtro de búsqueda
    estudiante = request.GET.get('estudiante')
    curso = request.GET.get('curso')
    estado = request.GET.get('estado')

    # Obtener todos los registros de la relación EstudianteCurso
    estudianteCurso = EstudianteCurso.objects.all()

    # Filtrar por nombre o apellidos de estudiante si hay búsqueda
    if estudiante:
        estudianteCurso = estudianteCurso.filter(estudiante__nombre__icontains=estudiante) | estudianteCurso.filter(estudiante__apellidos__icontains=estudiante)

    # Filtrar por curso si se selecciona uno
    if curso:
        estudianteCurso = estudianteCurso.filter(curso__id=curso)

    # Filtrar por estado si se selecciona uno
    if estado:
        estudianteCurso = estudianteCurso.filter(estado=estado)

    # Obtener todas las opciones para los desplegables
    cursos = EstudianteCurso.objects.values('curso__id', 'curso__nombre').distinct()
    estados = EstudianteCurso.objects.values('estado').distinct()

    return render(request, 'lista_est_cur.html', {
        'title': 'Relación estudiantes y curso',
        'estudiantes_cursos': estudianteCurso,
        'cursos': cursos,
        'estados': estados,
    })

# Vista para agregar o editar una relación de estudiante con curso
def formulario_estudiante_curso(request):
    if request.method == 'POST':
        form = EstudianteCursoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario
            return redirect('lista-estudiantes-cursos')  # Asegúrate de que este nombre coincida
    else:
        form = EstudianteCursoForm()  # Formulario vacío si no es POST

    return render(request, 'formulario_estudiante_curso.html', {'form': form})