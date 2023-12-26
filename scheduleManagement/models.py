from django.db import models
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify

class Horario(models.Model):
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse_lazy("detail_schedule", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """Create an automatic slug for the schedule."""

        self.slug = slugify(self.dia)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.dia} | {self.hora_inicio} - {self.hora_fim}"


class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    horario = models.OneToOneField(Horario, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse_lazy("detail_discipline", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """Create an automatic slug for the discipline."""

        self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    disciplinas = models.ManyToManyField(Disciplina)
    horario = models.OneToOneField(Horario, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse_lazy("detail_course", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        """Create an automatic slug for the course."""

        self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        """Returns the name of the course."""
        return self.nome
