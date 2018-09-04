import requests


def get_intent(query):
    url = 'http://127.0.0.1:8000'
    params = {'query': query}
    r = requests.get(url, params=params)
    books = r.json()
    books_list = {'books': books['results']}
    return books_list
