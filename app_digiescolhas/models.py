from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class DisciplinasDiurno(models.Model):
    codigo = models.CharField(max_length=20, null=True)
    componente = models.CharField(max_length=255, null=True)
    carga_horaria = models.PositiveIntegerField(null=True, validators=[MinValueValidator(64), MaxValueValidator(192)])
    natureza = models.CharField(max_length=50, null=True)
    semestre = models.PositiveIntegerField(null=True)
    id_matriz = models.PositiveIntegerField(null=True)

class DisciplinasNoturno(models.Model):
    codigo = models.CharField(max_length=20, null=True)
    componente = models.CharField(max_length=255, null=True)
    carga_horaria = models.PositiveIntegerField(null=True, validators=[MinValueValidator(64), MaxValueValidator(192)])
    natureza = models.CharField(max_length=50, null=True)
    semestre = models.PositiveIntegerField(null=True)
    id_matriz = models.PositiveIntegerField(null=True)
