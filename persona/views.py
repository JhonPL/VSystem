from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
from django.db.models import Q

# Vista para listar estudiantes
def get_estudiantes(request):
    query = request.GET.get('q')  # Obtiene el valor del campo de búsqueda
    if query:
        estudiantes = Persona.objects.filter(
            Q(rol='Estudiante') &  # Asegúrate de que sean estudiantes
            (Q(nombre__icontains=query) |  # Busca en nombre
             Q(apellidos__icontains=query) |  # Busca en apellidos
             Q(dni__icontains=query))  # Busca en DNI
        )
    else:
        estudiantes = Persona.objects.filter(rol='Estudiante')  # Muestra todos si no hay filtro

    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de Estudiantes',
        'estudiantes': estudiantes
    })

# Vista para agregar nuevos estudiantes
def formulario_estudiante(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)  # No guardar aún en la base de datos
            estudiante.rol = 'Estudiante'  # Asignar el rol predeterminado
            estudiante.save()  # Ahora guarda el estudiante
            return redirect('lista-estudiantes')  # Redirige a la lista de estudiantes después de guardar
    else:
        form = PersonaForm()

    return render(request, 'formulario_estudiantes.html', {'form': form})