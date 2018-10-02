from django.template import loader
from django.http import HttpResponse, JsonResponse
from .models import *
from datetime import date, datetime
from rest_framework.decorators import api_view
from .serializers import CursoSerializer
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def get_cursos(request):
    """
    Retrieve al cursos from graph
    :return: cursos in a string
    """
    if request.method == 'GET':
        cursos = Curso.nodes.all()
        cursos_list = ""
        for i in range(0, len(cursos)):
            # print(cursos[i].__dict__["nombre"])
            if i + 1 != len(cursos):
                cursos_list += cursos[i].__dict__["nombre"] + ", "
            else:
                cursos_list += cursos[i].__dict__["nombre"]
        return JsonResponse({"cursos": cursos_list})


@api_view(['GET'])
def get_curso_fecha_inicio(request):
    """
    Retrieve al cursos from graph
    :return: cursos in a string
    """
    if request.method == 'GET':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if "curso" in serializer.validated_data:
                try:
                    curso = Curso.nodes.get(nombre__icontains=serializer.validated_data["curso"])
                    resp = {"nombre_curso": curso.__dict__["nombre"], "fecha_inicio": curso.__dict__["fecha_inicio"]}
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                except Curso.DoesNotExist:
                    print("Cant find (CURSO) ", serializer.validated_data["curso"])
                    return JsonResponse({"error": "(CURSO) " + serializer.validated_data["curso"] + " not found "},
                                        status=status.HTTP_404_NOT_FOUND)
            if "codigo" in serializer.validated_data:
                try:
                    curso = Curso.nodes.get(cod__icontains=serializer.validated_data["codigo"])
                    resp = {"nombre_curso": curso.__dict__["nombre"], "fecha_inicio": curso.__dict__["fecha_inicio"]}
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                except Curso.DoesNotExist:
                    print("Cant find (CURSO) ", serializer.validated_data["codigo"])
                    return JsonResponse({"error": "(CURSO) " + serializer.validated_data["codigo"] + " not found "},
                                        status=status.HTTP_404_NOT_FOUND)
            if "synonym" in serializer.validated_data:
                try:
                    sinonimo = Sinonimo.nodes.get(sinonimo__icontains=serializer.validated_data["synonym"])
                    print(sinonimo.__dict__["curso"]["nombre"])
                    resp = {"nombre_curso": "WIP"}
                    # resp = {"nombre_curso": curso.__dict__["nombre"], "fecha_inicio": curso.__dict__["fecha_inicio"]}
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                except Curso.DoesNotExist:
                    print("Cant find (CURSO) ", serializer.validated_data["synonym"])
                    return JsonResponse({"error": "(CURSO) " + serializer.validated_data["synonym"] + " not found "},
                                        status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_curso_inscripcion(request):
    """
    Retrieve al cursos from graph
    :return: cursos in a string
    """
    if request.method == 'GET':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if "curso" in serializer.validated_data:
                try:
                    curso = Curso.nodes.get(nombre__icontains=serializer.validated_data["curso"])
                    resp = {"nombre_curso": curso.__dict__["nombre"], "link": curso.__dict__["link"]}
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                except Curso.DoesNotExist:
                    print("Cant find (CURSO) ", serializer.validated_data["curso"])
                    return JsonResponse({"error": "(CURSO) " + serializer.validated_data["curso"] + " not found "},
                                        status=status.HTTP_404_NOT_FOUND)
            if "codigo" in serializer.validated_data:
                try:
                    curso = Curso.nodes.get(cod__icontains=serializer.validated_data["codigo"])
                    resp = {"nombre_curso": curso.__dict__["nombre"], "link": curso.__dict__["link"]}
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                except Curso.DoesNotExist:
                    print("Cant find (CURSO) ", serializer.validated_data["codigo"])
                    return JsonResponse({"error": "(CURSO) " + serializer.validated_data["codigo"] + " not found "},
                                        status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_curso_prerequisitos(request):
    """
    Retrieve al cursos from graph
    :return: cursos in a string
    """
    if request.method == 'GET':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if "curso" in serializer.validated_data:
                try:
                    curso = Curso.nodes.get(nombre__icontains=serializer.validated_data["curso"])
                    resp = {"nombre_curso": curso.__dict__["nombre"],
                            "pre_requisitos": curso.__dict__["pre_requisitos"]}
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                except Curso.DoesNotExist:
                    print("Cant find (CURSO) ", serializer.validated_data["curso"])
                    return JsonResponse({"error": "(CURSO) " + serializer.validated_data["curso"] + " not found "},
                                        status=status.HTTP_404_NOT_FOUND)
            if "codigo" in serializer.validated_data:
                try:
                    curso = Curso.nodes.get(cod__icontains=serializer.validated_data["codigo"])
                    resp = {"nombre_curso": curso.__dict__["nombre"],
                            "pre_requisitos": curso.__dict__["pre_requisitos"]}
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                except Curso.DoesNotExist:
                    print("Cant find (CURSO) ", serializer.validated_data["codigo"])
                    return JsonResponse({"error": "(CURSO) " + serializer.validated_data["codigo"] + " not found "},
                                        status=status.HTTP_404_NOT_FOUND)
            if "synonym" in serializer.validated_data:
                try:
                    sinonimo = Sinonimo.nodes.get(sinonimo__icontains=serializer.validated_data["synonym"])
                    print(sinonimo.__dict__["curso"]["nombre"])
                    resp = {"nombre_curso": "WIP"}
                    # resp = {"nombre_curso": curso.__dict__["nombre"], "fecha_inicio": curso.__dict__["fecha_inicio"]}
                    return JsonResponse(resp, status=status.HTTP_200_OK)
                except Curso.DoesNotExist:
                    print("Cant find (CURSO) ", serializer.validated_data["synonym"])
                    return JsonResponse({"error": "(CURSO) " + serializer.validated_data["synonym"] + " not found "},
                                        status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)


def graph(request):
    """
    Graph test
    """

    # for i in range(0,len(cursos)):
    #     print(cursos[i]["nombre"])
    # date1 = datetime.strptime("2018-09-07", "%Y-%m-%d").date()
    # print(date1)
    # date2 = datetime.strptime("2018-10-07", "%Y-%m-%d").date()
    # print(date2)
    # curso = Curso(cod='CD', nombre="Ciencia de datos", sinonimos=["Ciencia de datos", "Ciencia datos"],
    #               descripcion="Este curso te enseñara \rtodo lo referente a los datos",
    #               pre_requisitos="Ninguno",
    #               edicion="Segunda",
    #               oferta="Septimebre 2018",
    #               fecha_inscripcion=date1,
    #               fecha_inicio=date2,
    #               esfuerzo_estimado="5",
    #               duracion="7",
    #               link="http://opencampus.utpl.edu.ec/courses/course-v1:UTPL+AMOCR3+2018_2/about",
    #               institucion="U")
    # curso.save()

    # curso = Curso.nodes.get(cod="EMP")
    # print(curso)
    # sinonimo1 = Sinonimo.nodes.get(sinonimo="Emprendimiento")
    # sinonimo2 = Sinonimo.nodes.get(sinonimo="Gestion")
    # sinonimo1.curso.connect(curso)
    # sinonimo2.curso.connect(curso)

    # docente1 = Docente(nombre="Andre Herrera", nivel_academico="CN").save()

    # docente1 = Docente.nodes.get(nombre="Andre Herrera")
    # docente1.delete()
    # print(docente1)

    # docente2 = Docente(nombre="Mark Zucaritas").save()

    # docente2 = Docente.nodes.get(nombre="Mark Zucaritas")
    # docente1.delete()
    # print(docente2)

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
    #
    # competencia1 = Competencia.nodes.get(competencia="El humanismo de cristo")
    # print(competencia1)
    # competencia2 = Competencia.nodes.get(competencia="Innovacion y emprendimiento")
    # print(competencia2)
    # competencia.delete()
    # competencia.delete()

    # cargar retos
    # reto1 = Reto(titulo_reto="Innova Extreme",descripcion="Esta es un reto de innovacion extrema").save()
    # reto2 = Reto(titulo_reto="Nuevo producto",descripcion="Genera un nuevo producto").save()
    # curso.reto.connect(reto1)
    # curso.reto.connect(reto2)
    # reto1.curso.connect(curso)
    # reto2.curso.connect(curso)
    #
    # reto = Reto.nodes.get(titulo_reto="Innova Extreme")
    # print(reto)
    # reto = Reto.nodes.get(titulo_reto="Nuevo producto")
    # print(reto)

    # cargar Contenido
    # contenido1 = Contenido(orden="0", contenido="Introduccion al emprendimiento").save()
    # contenido2 = Contenido(orden="1", contenido="Que es ser emprendedor").save()
    # contenido = Contenido.nodes.get(orden='0')
    # print(contenido)
    # contenido = Contenido.nodes.get(orden='1')
    # print(contenido)
    # curso.contenido.connect(contenido1)
    # curso.contenido.connect(contenido2)
    # contenido1.curso.connect(curso)
    # contenido2.curso.connect(curso)

    template = loader.get_template('cursoshandler/graph.html')
    context = {
        "person": "hola"
    }
    return HttpResponse(template.render(context, request))
