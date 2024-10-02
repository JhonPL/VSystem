from django.db import models
from persona.models import Persona
from django.core.exceptions import ValidationError

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Persona, on_delete=models.CASCADE) 
    create_at = models.DateTimeField(auto_now=True)

    def clean(self):
        
        if self.profesor.rol != 'Profesor':
            raise ValidationError(f'{self.profesor.nombre} {self.profesor.apellidos} no tiene el rol de Profesor.')

    def __str__(self):
        return f' {self.nombre} - {self.profesor.nombre} {self.profesor.apellidos}'

    class Meta:
        db_table = 'Curso'