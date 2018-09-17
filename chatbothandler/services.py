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

def generate_answer(intent):
    # intent["intent"]
    # intent["answer"]
    # intent["slots"]
    # TODO invertir el ordem, primero obtener la info del curso y luego usarla
    if intent["intent"] == "listarCursos":
        split_index = intent["answer"].find("|")
        # getting cursos info
        cursos = get_cursos()
        if split_index != -1:
            intent["answer"] = intent["answer"][0:split_index - 1] + cursos
    elif intent["intent"] == "fechaInicioCurso":
        answer_parts = intent["answer"].split("|")
        if len(intent["slots"]) > 0:
            if intent["slots"][0]["value"].find("-") == -1:
                print(intent["slots"][0]["value"])
                curso_name = clean_curso(intent["slots"][0]["value"])
                curso_resp = get_curso_fecha_inicio({"curso": curso_name})
                # getting curso fecha inicio
                if curso_resp is not None:
                    intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                        "fecha_inicio"] + answer_parts[2]
                # else:
                #     # TODO handle synonyms
                #     # try with name
                #     curso_name = clean_curso(intent["slots"][0]["rawValue"])
                #     curso_resp = get_curso_fecha_inicio({"synonym": curso_name})
                #     # getting curso fecha inicio
                #     if curso_resp is not None:
                #         intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                #             "fecha_inicio"] + answer_parts[2]
            else:
                curso_resp = get_curso_fecha_inicio({"codigo": intent["slots"][0]["value"]})
                # getting curso fecha inicio
                if curso_resp is not None:
                    intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                        "fecha_inicio"] + answer_parts[2]
                else:
                    intent["answer"] = "No se ha podido encontrar el curso con el codigo" + intent["slots"][0][
                        "value"]
    elif intent["intent"] == "inscripcionCurso":
            # TODO test this
        answer_parts = intent["answer"].split("|")
        if len(intent["slots"]) > 0:
            if intent["slots"][0]["value"].find("-") == -1:
                print(intent["slots"][0]["value"])
                curso_name = clean_curso(intent["slots"][0]["value"])
                curso_resp = get_curso_inscripcion({"curso": curso_name})
                # getting curso fecha inicio
                if curso_resp is not None:
                     intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                        "link"] + answer_parts[2]
                else:
                    intent["answer"] = "No se ha podido encontrar el curso " + intent["slots"][0][
                        "value"]
            else:
                curso_resp = get_curso_inscripcion({"codigo": intent["slots"][0]["value"]})
                if curso_resp is not None:
                    intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                        "link"] + answer_parts[2]
                else:
                    intent["answer"] = "No se ha podido encontrar el curso con el codigo" + intent["slots"][0][
                        "value"]
        else:
            print("Slot not found")
    return intent
