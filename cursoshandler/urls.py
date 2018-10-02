from django.urls import path
from cursoshandler import views


urlpatterns = [
    path(r'graph/', views.graph, name='graph'),
    path(r'all/', views.get_cursos, name='get_cursos'),
    path(r'fecha-inicio/', views.get_curso_fecha_inicio, name='get_curso_fecha_inicio'),
    path(r'inscripcion/', views.get_curso_inscripcion, name='get_curso_inscripcion'),
    path(r'prerrequisitos/', views.get_curso_prerequisitos, name='get_curso_prerequisitos'),
]
