from django.template import loader
from django.http import HttpResponse
from .models import *
from datetime import date, datetime


# Create your views here.
# people = Person.create_or_update(
#     {'name': 'Tim', 'age': 83},
#     {'name': 'Bob', 'age': 23},
#     {'name': 'Jill', 'age': 34},
# )
def graph(request):
    """
    Graph test
    """
    # date1 = datetime.strptime("2018-09-06", "%Y-%m-%d").date()
    # print(date1)
    # date2 = datetime.strptime("2018-10-06", "%Y-%m-%d").date()
    # print(date2)
    # curso = Curso(cod='EMP', nombre="EMPRENDIMIENTO Y GESTION", sinonimos=["Emprendimiento", "Innovacion"],
    #               descripcion="Este curso trata de dar las herramientas necesarias para emprender",
    #               pre_requisitos="Ninguno",
    #               edicion="Primera",
    #               oferta="Septimebre 2018",
    #               fecha_inscripcion=date1,
    #               fecha_inicio=date2,
    #               esfuerzo_estimado="6",
    #               duracion="6",
    #               link="http://opencampus.utpl.edu.ec/courses/course-v1:UTPL+AIRPOLLUTION8+2018_2/about",
    #               institucion="U")
    # curso.save()
    curso = Curso.nodes.get(cod="EMP")
    print(curso)

    # docente1 = Docente(nombre="Andre Herrera", nivel_academico="CN").save()

    docente1 = Docente.nodes.get(nombre="Andre Herrera")
    # docente1.delete()
    print(docente1)

    # docente2 = Docente(nombre="Mark Zucaritas").save()

    docente2 = Docente.nodes.get(nombre="Mark Zucaritas")
    # docente1.delete()
    print(docente2)

    # curso.docente.connect(docente1)
    # curso.docente.connect(docente2)
    # docente1.curso.connect(curso)
    # docente2.curso.connect(curso)

    # cargar competencias
    # competencia1 = Competencia(competencia="El humanismo de cristo").save()
    # competencia.delete()
    # competencia2 = Competencia(competencia="Innovacion y emprendimiento").save()
    # competencia.delete()

    # curso.competencia.connect(competencia1)
    # curso.competencia.connect(competencia2)
    # competencia1.curso.connect(curso)
    # competencia2.curso.connect(curso)

    competencia1 = Competencia.nodes.get(competencia="El humanismo de cristo")
    print(competencia1)
    competencia2 = Competencia.nodes.get(competencia="Innovacion y emprendimiento")
    print(competencia2)
    # competencia.delete()
    # competencia.delete()

    # cargar retos
    # reto1 = Reto(titulo_reto="Innova Extreme",descripcion="Esta es un reto de innovacion extrema").save()
    # reto2 = Reto(titulo_reto="Nuevo producto",descripcion="Genera un nuevo producto").save()
    # curso.reto.connect(reto1)
    # curso.reto.connect(reto2)
    # reto1.curso.connect(curso)
    # reto2.curso.connect(curso)

    reto = Reto.nodes.get(titulo_reto="Innova Extreme")
    print(reto)
    reto = Reto.nodes.get(titulo_reto="Nuevo producto")
    print(reto)

    # cargar Contenido
    # contenido1 = Contenido(orden="0", contenido="Introduccion al emprendimiento").save()
    # contenido2 = Contenido(orden="1", contenido="Que es ser emprendedor").save()
    contenido = Contenido.nodes.get(orden='0')
    print(contenido)
    contenido = Contenido.nodes.get(orden='1')
    print(contenido)
    # curso.contenido.connect(contenido1)
    # curso.contenido.connect(contenido2)
    # contenido1.curso.connect(curso)
    # contenido2.curso.connect(curso)

    template = loader.get_template('cursoshandler/graph.html')
    context = {
        "person": "hola"
    }
    return HttpResponse(template.render(context, request))
