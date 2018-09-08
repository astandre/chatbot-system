from django.urls import path
from cursoshandler import views


urlpatterns = [
    path(r'graph/', views.graph, name='graph'),
    path(r'all/', views.get_cursos, name='get_cursos'),
]
