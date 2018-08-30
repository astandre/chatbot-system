from django.db import models
from datetime import datetime


# Create your models here.


class Docentes(models.Model):
    TERCER = 'TN'
    CUARTO = 'CN'
    TECNICO = 'T'
    N_ACADEMICO = (
        (TECNICO, 'Nivel Técnico'),
        (TERCER, 'Tercer Nivel'),
        (CUARTO, 'Cuarto Nivel')
    )

    id_docente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300, null=False)
    nivel_academico = models.CharField(
        null=False,
        max_length=2,
        choices=N_ACADEMICO,
        default=TERCER
    )
    email = models.EmailField(blank=True)
    twitter = models.CharField(blank=True, max_length=120)
    resumen = models.CharField(max_length=400, null=False)

    class Meta:
        default_related_name = 'docentes'
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
        db_table = 'docentes'

    def __str__(self):
        return self.nombre


class Cursos(models.Model):
    id_curso = models.AutoField(primary_key=True)
    cod = models.CharField(max_length=10, null=False, blank=False)
    nombre = models.CharField(max_length=60, null=False)
    descripcion = models.CharField(max_length=300, null=False, blank=True)
    pre_requisitos = models.CharField(max_length=300, null=False, blank=True)
    edicion = models.CharField(max_length=3, blank=False, default=1)
    oferta = models.CharField(max_length=20, blank=False)
    tematica = models.CharField(max_length=60, blank=False)
    fecha_inscripcion = models.DateField(blank=False, default=datetime.now)
    fecha_inicio = models.DateField(blank=False, default=datetime.now)
    esfuerzo_estimado = models.CharField(max_length=2, blank=False, default=1)
    duracion = models.CharField(max_length=2, blank=False, default=1)
    link = models.CharField(max_length=100, blank=False, default="http://opencampus.utpl.edu.ec/")
    UTPL = 'UTPL'
    OTRO = 'Otro'
    INSTITUCIONES = (
        (UTPL, 'UTPL'),
        (OTRO, 'Otro'),
    )
    institucion = models.CharField(
        null=False,
        max_length=5,
        choices=INSTITUCIONES,
        default=UTPL
    )
    archivado = models.BooleanField(default=False)
    docentes = models.ManyToManyField(Docentes, blank=True)

    class Meta:
        default_related_name = 'cursos'
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        db_table = 'cursos'

    def __str__(self):
        return self.nombre


class Competencias(models.Model):
    id_competencia = models.AutoField(primary_key=True)
    competencia = models.CharField(max_length=400, null=False)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_related_name = 'competencias'
        verbose_name = "Competencia"
        verbose_name_plural = "Competencias"
        db_table = 'competencias'

    def __str__(self):
        return self.competencia


class Retos(models.Model):
    id_reto = models.AutoField(primary_key=True)
    titulo_reto = models.CharField(max_length=30)
    fecha_inicio = models.DateTimeField(null=False, default=datetime.now)
    fecha_fin = models.DateTimeField(null=False, default=datetime.now)
    descripcion = models.CharField(max_length=400, null=False, blank=False)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_related_name = 'retos'
        verbose_name = "Reto"
        verbose_name_plural = "Retos"
        db_table = 'retos'

    def __str__(self):
        return self.titulo_reto


class Contenidos(models.Model):
    id_contenido = models.AutoField(primary_key=True)
    orden = models.CharField(max_length=2, blank=False)
    contenido = models.CharField(max_length=400, null=False)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_related_name = 'contenidos'
        verbose_name = "Contenido"
        verbose_name_plural = "Contenidos"
        db_table = 'contenidos'

    def __str__(self):
        return self.contenido


class SinonimosCurso(models.Model):
    id_sinonimo = models.AutoField(primary_key=True)
    sinonimo = models.CharField(max_length=400, null=False)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        default_related_name = 'sinonimoscurso'
        verbose_name = "SinonimoCurso"
        verbose_name_plural = "SinonimoCursos"
        db_table = 'sinonimos_curso'

    def __str__(self):
        return self.sinonimo
