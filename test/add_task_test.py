import requests

def test_add():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 203
    assert response_body['completed'] == False



def test_add_new():
    """
    Создать задачу, проставить отметку о выполнении и проверить что completed ==True
    :return:
    """
    body = {"title":"general","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {"completed":True}
    requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    assert response.status_code == 200
    assert response.json()['completed'] == True