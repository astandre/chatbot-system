from .services import *
from .models import Answers, EntityCheck, Intents


def intent_handler(intent):
    # intent["intent"]
    # intent["answer"]
    # intent["slots"]
    intent["answer"] = Answers.objects.values('answer').get(intent__name=intent["intent"])["answer"]
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
        if curso_name is None:
            if len(intent["context"]) > 0:
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
                intent["answer"] = "No se ha podido encontrar el curso " + curso_name
        else:
            print("Curso name not found")
    elif intent["intent"] == "inscripcionCurso":
        curso_name = None
        if len(intent["context"]) > 0:
            for value in intent["context"]:
                if value["entity"] == "curso":
                    curso_name = clean_curso(value["value"])
                    break
        if curso_name is not None:
            curso_resp = get_curso_inscripcion({"curso": curso_name})
            print(curso_resp)
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
                intent["answer"] = "No se ha podido encontrar el curso " + curso_name
    elif intent["intent"] == "duracionCurso":
        curso_name = None
        if len(intent["context"]) > 0:
            for value in intent["context"]:
                if value["entity"] == "curso":
                    curso_name = clean_curso(value["value"])
                    break
        if curso_name is not None:
            # getting curso_duracion
            # TODO get duracion
            curso_resp = get_curso_inscripcion({"curso": curso_name})
            if curso_resp is not None:
                answer_parts = intent["answer"].split("|")
                intent["answer"] = answer_parts[0] + curso_resp["nombre_curso"] + answer_parts[1] + curso_resp[
                    "link"] + answer_parts[2]
                if "context_vars" in intent:
                    intent.pop("context_vars", None)
                intent["solved"] = True
            else:
                intent["answer"] = "No se ha podido encontrar el curso " +curso_name
        else:
            print("Curso name not found")
    elif intent["intent"] == "prerrequitosCurso":
        curso_name = None
        if len(intent["context"]) > 0:
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
                intent["answer"] = "No se ha podido encontrar el curso " + curso_name
        else:
            print("Curso name not found")
    return intent


def resolve_missing_entities(intent):
    answer = Intents.objects.values('id_intent').get(name=intent['intent'])

    check_entity_list = list(EntityCheck.objects.values('entity__entity', 'clear_question', 'options').filter(
        intent__id_intent=answer["id_intent"]))
    slots = []
    context_vars = []
    if "slots" in intent:
        if len(intent["slots"]) == 0 and len(check_entity_list) > 0:
            for check_entity in check_entity_list:
                context_vars.append(
                    {"question": check_entity["clear_question"], "entity": check_entity["entity__entity"],
                     "options": check_entity["options"]})
    else:
        for check_entity in check_entity_list:
            if "slots" in intent:
                for slot in intent["slots"]:
                    if slot["entity"] == check_entity['entity__entity']:
                        slots.append({"entity": slot["entity"], "value": slot["value"]["value"]})
                        intent["slots"].remove(slot)
                        break
                for slot in intent["slots"]:
                    if slot["entity"] != check_entity['entity__entity']:
                        context_vars.append({"question": check_entity["clear_question"], "entity": slot["entity"],
                                             "options": check_entity["options"]})
                        break
    if len(context_vars) > 0:
        intent["context_vars"] = context_vars
    intent['slots'] = []
    return intent


def check_entities(intent):
    answer = Intents.objects.values('id_intent').get(name=intent['intent'])

    check_entity_list = list(EntityCheck.objects.values('entity__entity', 'clear_question', 'options').filter(
        intent__id_intent=answer["id_intent"]))
    state = False
    if len(check_entity_list) > 0:
        if "slots" in intent:
            if len(intent["slots"]) > 0:
                for slot in intent["slots"]:
                    print("SLOT CHEKING " + slot["entity"])
                    for entity_check in check_entity_list:
                        print(entity_check)
                        if slot["entity"] != entity_check["entity__entity"]:
                            state = False
                            break

        elif len(intent["context"]) > 0:
            state = True
            for context_value in intent["context"]:
                print("CONTEXT CHEKING " + context_value["entity"])
                for entity_check in check_entity_list:
                    print(entity_check)
                    if context_value["entity"] != entity_check["entity__entity"]:
                        state = False
                        break
            state = True

        return state
    else:
        return True


def slots_to_context(intent):
    if "slots" in intent:
        if len(intent["slots"]) > 0:
            for slot in intent["slots"]:
                add = True
                for i in range(0, len(intent["context"])):
                    if slot["entity"] == intent["context"][i]["entity"]:
                        intent["context"][i]["value"] = slot["value"]["value"]
                        add = False
                        break
                if add:
                    intent["context"].append({"value": slot["value"]["value"], "entity": slot["entity"]})
            intent['slots'] = []
    return intent
