import requests

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


def generate_answer(intent):
    # intent["intent"]
    # intent["answer"]
    # intent["slots"]
    split_index = intent["answer"].find("|")
    print(split_index)
    if intent["intent"] == "listarCursos":
        # retrieve cursos
        cursos = get_cursos()
        if split_index != -1:
            intent["answer"] = intent["answer"][0:split_index - 1] + cursos
    return intent
