from django.db import models

class Horario(models.Model):
  dia = models.DateField()
  horarioInicio = models.TimeField()
  horarioTermino = models.TimeField()
  
  def __str__(self):
    return f'{self.dia} | {self.horarioInicio} - {self.horarioTermino}'

class Disciplina(models.Model):
  nome = models.CharField(max_length=255)
  codigo = models.CharField(max_length=255)
  horario = models.OneToOneField(Horario, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.nome
  
class Curso(models.Model):
  nome = models.CharField(max_length=255)
  codigo = models.CharField(max_length=255)
  disciplinas = models.ManyToManyField(Disciplina)
  horario = models.OneToOneField(Horario, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.nome
