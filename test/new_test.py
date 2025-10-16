import requests

def test_add():
    body = {"title":"Mihail","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response_body["id"]
    print(response_body)

    assert response.status_code ==200

    body = {"title": "Mihail_edited", "completed": False}
    response = requests.patch(f"https://todo-app-sky.herokuapp.com/{id}", json=body)
    local_id = response.json()["id"]

    response = requests.get(f'https://todo-app-sky.herokuapp.com/{local_id}')
    assert response.status_code == 200
    assert id == local_id