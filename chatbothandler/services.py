import requests
from .utils import clean_curso

BASE_URL = "http://127.0.0.1:8000"


# TODO parametrizar
def get_intent(query):
    url = BASE_URL + '/engine/resolve/'
    json = {'query': query}
    r = requests.post(url, json=json)
    intent = r.json()
    return intent


def get_intent_answer(intent_name):
    url = BASE_URL + '/engine/answer/'
    json = {'intent': intent_name}
    r = requests.get(url, json=json)
    intent = r.json()
    return intent


def get_cursos():
    url = BASE_URL + '/cursos/all/'
    r = requests.get(url)
    response = r.json()
    return response["cursos"]


def get_curso_fecha_inicio(json):
    url = BASE_URL + '/cursos/fecha-inicio/'
    r = requests.get(url, json=json)
    if r.status_code == 200:
        response = r.json()
    else:
        response = None
    return response


def get_curso_inscripcion(json):
    url = BASE_URL + '/cursos/inscripcion/'
    r = requests.get(url, json=json)
    if r.status_code == 200:
        response = r.json()
    else:
        response = None
    return response


def get_curso_prerrequisitos(json):
    url = BASE_URL + '/cursos/prerrequisitos/'
    r = requests.get(url, json=json)
    if r.status_code == 200:
        response = r.json()
    else:
        response = None
    return response

