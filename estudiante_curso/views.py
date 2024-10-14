from django.shortcuts import render, redirect
from .models import EstudianteCurso
from .forms import EstudianteCursoForm

# Vista para listar los estudiantes y cursos
def Estudiante_Curso(request):
    estudiante = request.GET.get('estudiante')
    curso = request.GET.get('curso')
    estado = request.GET.get('estado')

    
    estudianteCurso = EstudianteCurso.objects.all()

    
    if estudiante:
        estudianteCurso = estudianteCurso.filter(estudiante__nombre__icontains=estudiante) | estudianteCurso.filter(estudiante__apellidos__icontains=estudiante)

    if curso:
        estudianteCurso = estudianteCurso.filter(curso__id=curso)

    
    if estado:
        estudianteCurso = estudianteCurso.filter(estado=estado)

    
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
            form.save()  
            return redirect('lista-estudiantes-cursos')  
    else:
        form = EstudianteCursoForm()  

    return render(request, 'formulario_estudiante_curso.html', {'form': form})