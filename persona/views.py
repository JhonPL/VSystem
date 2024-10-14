from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm
from django.db.models import Q

# Vista para listar estudiantes
def get_estudiantes(request):
    query = request.GET.get('q')  
    if query:
        estudiantes = Persona.objects.filter(
            Q(rol='Estudiante') &  
            (Q(nombre__icontains=query) |  
             Q(apellidos__icontains=query) |  
             Q(dni__icontains=query))  
        )
    else:
        estudiantes = Persona.objects.filter(rol='Estudiante')  

    return render(request, 'lista-estudiantes.html', {
        'title': 'Lista de Estudiantes',
        'estudiantes': estudiantes
    })

# Vista para agregar nuevos estudiantes
def formulario_estudiante(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)  
            estudiante.rol = 'Estudiante'  
            estudiante.save()  
            return redirect('lista-estudiantes')  
    else:
        form = PersonaForm()

    return render(request, 'formulario_estudiantes.html', {'form': form})