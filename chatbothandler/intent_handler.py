from .services import *
from .models import Answers


def intent_handler(intent):
    # intent["intent"]
    # intent["answer"]
    # intent["slots"]
    intent["answer"] = Answers.objects.get(intent__name=intent["intent"])
    if intent["intent"] == "listarCursos":
        # getting cursos info
        cursos = get_cursos()
        full_answer = ""
        for i in range(0, len(cursos)):
            if i + 1 != len(cursos):
                full_answer += cursos[i] + ", "
            else:
                full_answer += cursos[i]
        intent["answer"] += full_answer
    elif intent["intent"] == "fechaInicioCurso":
        curso_name = None
        if "slots" in intent and len(intent["slots"]) > 0:
            curso_name = clean_curso(intent["slots"][0]["value"])
        if curso_name is None:
            if "context" in intent and len(intent["context"]) > 0:
                for value in intent["context"]:
                    if value["entity"] == "curso":
                        curso_name = clean_curso(value["value"])
                        break
        if curso_name is not None:
            curso_resp = get_curso_fecha_inicio({"curso": curso_name})
            # getting curso fecha inicio
            if curso_resp is not None:
                answer_parts = intent["answer"].split("|")
                intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                    "fecha_inicio"] + answer_parts[2]
                if "context_vars" in intent:
                    intent.pop("context_vars", None)
                intent["solved"] = True
            else:
                intent["answer"] = "No se ha podido encontrar el curso " + intent["slots"][0][
                    "value"]
        else:
            print("Curso name not found")
    elif intent["intent"] == "inscripcionCurso":
        curso_name = None
        if "slots" in intent and len(intent["slots"]) > 0:
            curso_name = clean_curso(intent["slots"][0]["value"])
        if curso_name is None:
            if "context" in intent and len(intent["context"]) > 0:
                for value in intent["context"]:
                    if value["entity"] == "curso":
                        curso_name = clean_curso(value["value"])
                        break
        if curso_name is not None:
            curso_resp = get_curso_inscripcion({"curso": curso_name})
            # getting curso fecha inicio
            if curso_resp is not None:
                #     Get intent answer
                answer_parts = intent["answer"].split("|")
                intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                    "link"] + answer_parts[2]
                if "context_vars" in intent:
                    intent.pop("context_vars", None)
                intent["solved"] = True
            else:
                intent["answer"] = "No se ha podido encontrar el curso " + intent["slots"][0][
                    "value"]
    elif intent["intent"] == "duracionCurso":
        curso_name = None
        if "slots" in intent and len(intent["slots"]) > 0:
            curso_name = clean_curso(intent["slots"][0]["value"])
        if curso_name is None:
            if "context" in intent and len(intent["context"]) > 0:
                for value in intent["context"]:
                    if value["entity"] == "curso":
                        curso_name = clean_curso(value["value"])
                        break
        if curso_name is not None:
            curso_resp = get_curso_inscripcion({"curso": curso_name})
            # getting curso_duracion
            if curso_resp is not None:
                answer_parts = intent["answer"].split("|")
                intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                    "link"] + answer_parts[2]
                if "context_vars" in intent:
                    intent.pop("context_vars", None)
                intent["solved"] = True
            else:
                intent["answer"] = "No se ha podido encontrar el curso " + intent["slots"][0][
                    "value"]
        else:
            print("Curso name not found")
    elif intent["intent"] == "prerrequitosCurso":
        curso_name = None
        if "slots" in intent and len(intent["slots"]) > 0:
            curso_name = clean_curso(intent["slots"][0]["value"])
        if curso_name is None:
            if "context" in intent and len(intent["context"]) > 0:
                for value in intent["context"]:
                    if value["entity"] == "curso":
                        curso_name = clean_curso(value["value"])
                        break
        if curso_name is not None:
            # getting curso prerrequisitos
            curso_resp = get_curso_prerrequisitos({"curso": curso_name})
            if curso_resp is not None:
                #     Get intent answer
                answer_parts = intent["answer"].split("|")
                intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                    "pre_requisitos"] + answer_parts[2]
                if "context_vars" in intent:
                    intent.pop("context_vars", None)
                intent["solved"] = True
            else:
                intent["answer"] = "No se ha podido encontrar el curso " + intent["slots"][0][
                    "value"]
        else:
            print("Curso name not found")
    return intent
