import requests
from config import base_url, headers, title


def test_create_project():
    body={
    "title": title
    }
    r = requests.post(base_url+"/projects", json=body, headers=headers)
    assert r.status_code == 201

def test_change_project():
    body={
    "title": title
    }
    r = requests.post(base_url+"/projects", json=body, headers=headers)
    assert r.status_code == 201
    id=r.json()["id"]
    body2={
        "title": "Новое название"
    }
    r2=requests.put(base_url+"/projects/"+id, json=body2, headers=headers)
    assert r2.status_code == 200

def test_get_project():
    body = {
        "title": title
    }
    r = requests.post(base_url + "/projects", json=body, headers=headers)
    assert r.status_code == 201
    id = r.json()["id"]
    r2 = requests.get(base_url + "/projects/" + id, headers=headers)
    assert r2.status_code == 200
    assert r2.json()["title"] == "Новый проект"

# негативные
def test_create_project_negative():
    body={
    "title": title
    }
    r = requests.post(base_url+"/projects", json=body, headers=headers)
    assert r.status_code == 400

def test_change_project_negative():
    id="2354"
    body2={
        "title": "Новое название"
    }
    r2=requests.put(base_url+"/projects/"+id, json=body2, headers=headers)
    assert r2.status_code == 404

def test_get_project_negative():
    id = "5678"
    r2 = requests.get(base_url + "/projects/" + id, headers=headers)
    assert r2.status_code == 404