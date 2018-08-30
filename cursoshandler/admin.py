from django.contrib import admin
from .models import *


# Register your models here.
class CompetenciasInline(admin.TabularInline):
    model = Competencias
    extra = 3


class RetosInline(admin.TabularInline):
    model = Retos
    extra = 3


class ContenidosInline(admin.TabularInline):
    model = Contenidos
    extra = 3


class SinonimosCursoInline(admin.TabularInline):
    model = SinonimosCurso
    extra = 3


class DocentesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel_academico', 'email')
    list_filter = ['nivel_academico']
    search_fields = ['nombre']


class CursosAdmin(admin.ModelAdmin):
    inlines = [CompetenciasInline, RetosInline, ContenidosInline, SinonimosCursoInline]
    list_display = ('nombre', 'edicion', 'fecha_inscripcion', 'fecha_inicio', 'institucion')
    list_filter = ['edicion', 'oferta', 'tematica', 'institucion','docentes__nombre']
    search_fields = ['nombre']


class CompetenciasAdmin(admin.ModelAdmin):
    list_display = ('competencia', 'curso')
    list_filter = ['curso__nombre', ]
    search_fields = ['competencia']


class RetosAdmin(admin.ModelAdmin):
    list_display = ('titulo_reto', 'fecha_inicio', 'fecha_fin',)
    list_filter = ['curso__nombre']
    search_fields = ['titulo_reto']


class ContenidosAdmin(admin.ModelAdmin):
    list_display = ('orden', 'contenido', 'curso')
    list_filter = ['orden', 'curso__nombre']
    search_fields = ['contenido']


class SinonimosCursoAdmin(admin.ModelAdmin):
    list_filter = ['curso__nombre']
    search_fields = ['sinonimo']


admin.site.register(Cursos, CursosAdmin)
admin.site.register(Docentes, DocentesAdmin)
admin.site.register(Competencias, CompetenciasAdmin)
admin.site.register(Retos, RetosAdmin)
admin.site.register(Contenidos, ContenidosAdmin)
admin.site.register(SinonimosCurso, SinonimosCursoAdmin)
