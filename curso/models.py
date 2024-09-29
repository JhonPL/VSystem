from django.db import models
from persona.models import Persona

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Persona, on_delete=models.CASCADE) 
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.nombre} - {self.profesor.nombre} {self.profesor.apellidos}'

    class Meta:
        db_table = 'Curso'