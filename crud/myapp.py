#This is third party app it will be in any language i take in python
import requests
import json

URL = "http://127.0.0.1:8000/userapi/"

#Request For getting data
def get_data(id = None):
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)
get_data()

#Request for creating data
def post_data():
    data = {
        'text' :'Reading'
        #'lastname' : 'Sharma',
        #'email' : 'tina@gmail.com'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

post_data()

#Request for updating data
def update_data():
    data = {
        'id':1,
        'text':'Writing'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
update_data()

#Request for deleting data
def delete_data():
    data = {'id':1}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
delete_data()


