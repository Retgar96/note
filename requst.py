import requests
import settings

def create_new_index(user_id):
    answer = requests.get(f'{settings.url_elastic}_cat/indices/user_1297710219')
    try:
        print(answer.json())
    except:
        answer_true = requests.put(f'{settings.url_elastic}user_{user_id}')
        print(answer_true.json())

def add_note(user_id, message):
    params = { "note" : f"{message}" }
    answer = requests.post(f'{settings.url_elastic}user_{user_id}', params=params)



def search_note(user_id, query):
    params = {"query":{"term":{"note": f"{query}"}}}
    result = requests.post(f'{settings.url_elastic}/user_{user_id}_search', data=params)
    return result