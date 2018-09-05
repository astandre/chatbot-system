import requests


# TODO parametrizar
def get_intent(query):
    url = 'http://127.0.0.1:8000/engine/resolve/'
    json = {'query': query}
    r = requests.post(url, json=json)
    intent = r.json()
    return intent
