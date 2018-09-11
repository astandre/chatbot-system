from django.urls import path
from cursoshandler import views


urlpatterns = [
    path(r'graph/', views.graph, name='graph'),
    path(r'all/', views.get_cursos, name='get_cursos'),
    path(r'fecha-inicio/', views.get_curso_fecha_inicio, name='get_curso_fecha_inicio'),
]
