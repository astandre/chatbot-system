from django.urls import path
from cursoshandler import views


urlpatterns = [
    path(r'graph/', views.graph, name='graph'),
]
